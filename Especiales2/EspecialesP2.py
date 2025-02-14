import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Esta función define el sistema de ecuaciones diferenciales del oscilador armónico simple.
def osciladorArmonico(t, y, k, m):
    x, v = y
    dxdt = v
    dvdt = -k/m * x
    return [dxdt, dvdt]

#La función solve_ivp 
# se utiliza para resolver ecuaciones diferenciales ordinarias (EDO) 
# Limites: Una tupla (T0,Tf) que define el intervalo de integración desde el tiempo inicial 
# CondicionesIniciales: Un array que contiene las condiciones iniciales para las variables dependientes.
#La salida de solve_ivp es un objeto que contiene la solución del sistema de ecuaciones diferenciales. Los atributos más importantes son:
# t: Los puntos de tiempo en los que se evaluó la solución.
# y: La solución del sistema en los puntos de tiempo correspondientes.
#FuncionSolucion: Una función que permite evaluar la solución en cualquier punto dentro del intervalo de integración. 

def resolverOsciladorArmonico(PosicionInicial, VelocidadInicial, ConstanteResorteK, Masa, TiempoFinal):
    CondicionesIniciales = [PosicionInicial, VelocidadInicial]
    Limites = (0, TiempoFinal)
    FuncionSolucion = solve_ivp(osciladorArmonico, Limites, CondicionesIniciales, args=(ConstanteResorteK, Masa), dense_output=True)
    return FuncionSolucion

def graficar_resultados(FuncionSolucion, TiempoFinal):
    t = np.linspace(0, TiempoFinal, 300)
    z = FuncionSolucion.sol(t)
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, TiempoFinal)
    ax.set_ylim(min(min(z[0]), min(z[1])) - 1, max(max(z[0]), max(z[1])) + 1)
    line1, = ax.plot([], [], label='Posición (x)')
    line2, = ax.plot([], [], label='Velocidad (v)')
    
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return line1, line2
    
    def update(frame):
        line1.set_data(t[:frame], z[0][:frame])
        line2.set_data(t[:frame], z[1][:frame])
        return line1, line2
    
    ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Magnitud')
    plt.title('Oscilador Armónico Simple')
    plt.legend()
    plt.grid()
    
    # Integrar el gráfico en la interfaz Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    return canvas

def obtener_valores():
    PosicionInicial = float(posicion_inicial_entry.get())
    VelocidadInicial = float(velocidad_inicial_entry.get())
    ConstanteResorteK = float(constante_resorte_entry.get())
    Masa = float(masa_entry.get())
    TiempoFinal = float(tiempo_final_entry.get())
    
    # Calcular la frecuencia angular
    omega = np.sqrt(ConstanteResorteK / Masa)
    
    # Redondear los valores a un máximo de dos decimales
    PosicionInicial = round(PosicionInicial, 2) if PosicionInicial % 1 != 0 else int(PosicionInicial)
    VelocidadInicial = round(VelocidadInicial, 2) if VelocidadInicial % 1 != 0 else int(VelocidadInicial)
    omega = round(omega, 2) if omega % 1 != 0 else int(omega)
    
    # Definir las funciones x(t) y v(t) en formato texto
    #x(t)=Acos(ωt)+Bsin(ωt)  --> en x(0) = A --> A es la posiciónInicial. Si derivo.. v(0)= Bω --> B= v(0)/w  osea Velocidad Inicial / frecuencia angular 
    #x(t) = {PosicionInicial}*cos({omega} t) + {VelocidadInicial}/{omega} sin({omega} t)
    #v(t)= -wA.sen (wt)
    #v(t)=−x(0)ω sin(ωt) + v(0).cos(ωt)
    #v(t) = -{PosicionInicial}*{omega} sin({omega} t) + {VelocidadInicial} cos({omega} t)

    x_t_func_parts = []
    if PosicionInicial != 0:
        x_t_func_parts.append(f"{PosicionInicial} cos({omega} t)")
    if VelocidadInicial != 0:
        x_t_func_parts.append(f"{VelocidadInicial}/{omega} sin({omega} t)")
    
    x_t_func = " + ".join(x_t_func_parts)
    
    v_t_func_parts = []
    if PosicionInicial != 0:
        v_t_func_parts.append(f"-{PosicionInicial * omega} sin({omega} t)")
    if VelocidadInicial != 0:
        v_t_func_parts.append(f"{VelocidadInicial} cos({omega} t)")
    
    v_t_func = " + ".join(v_t_func_parts)
    
    # Mostrar las funciones en la interfaz gráfica
    x_t_label.config(text=f"x(t) = {x_t_func}")
    v_t_label.config(text=f"v(t) = {v_t_func}")
    
    FuncionSolucion = resolverOsciladorArmonico(PosicionInicial, VelocidadInicial, ConstanteResorteK, Masa, TiempoFinal)
    
    # Limpiar el gráfico anterior si existe
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    
    canvas = graficar_resultados(FuncionSolucion, TiempoFinal)

def limpiar_campos():
    posicion_inicial_entry.delete(0, tk.END)
    velocidad_inicial_entry.delete(0, tk.END)
    constante_resorte_entry.delete(0, tk.END)
    masa_entry.delete(0, tk.END)
    tiempo_final_entry.delete(0, tk.END)
    x_t_label.config(text="Función x(t):")
    v_t_label.config(text="Función v(t):")
    global canvas
    if canvas:
        canvas.get_tk_widget().pack_forget()
    canvas = None

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulación de Oscilador Armónico Simple")

# Ajustar el tamaño de la ventana
root.geometry("550x700")  # Ancho x Alto
root.minsize(400, 300)    # Tamaño mínimo
root.maxsize(800, 800)    # Tamaño máximo


# Crear un frame para los controles
frame_controles = tk.Frame(root)
frame_controles.pack(anchor=tk.N, padx=20, pady=20)

# Entrada para la posición inicial
posicion_inicial_label = tk.Label(frame_controles, text="Posición Inicial (m)")
posicion_inicial_label.pack()
posicion_inicial_entry = tk.Entry(frame_controles)
posicion_inicial_entry.pack()

# Entrada para la velocidad inicial
velocidad_inicial_label = tk.Label(frame_controles, text="Velocidad Inicial (m/s)")
velocidad_inicial_label.pack()
velocidad_inicial_entry = tk.Entry(frame_controles)
velocidad_inicial_entry.pack()

# Entrada para la constante del resorte
constante_resorte_label = tk.Label(frame_controles, text="Constante del Resorte (N/m)")
constante_resorte_label.pack()
constante_resorte_entry = tk.Entry(frame_controles)
constante_resorte_entry.pack()

# Entrada para la masa
masa_label = tk.Label(frame_controles, text="Masa (kg)")
masa_label.pack()
masa_entry = tk.Entry(frame_controles)
masa_entry.pack()

# Entrada para el tiempo final
tiempo_final_label = tk.Label(frame_controles, text="Tiempo Final (s)")
tiempo_final_label.pack()
tiempo_final_entry = tk.Entry(frame_controles)
tiempo_final_entry.pack()

# Botón para obtener los valores y resolver la ecuación
submit_button = tk.Button(frame_controles, text="Resolver", command=obtener_valores)
submit_button.pack()

# Etiquetas para mostrar las funciones x(t) y v(t)
x_t_label = tk.Label(frame_controles, text="Función x(t):")
x_t_label.pack()
v_t_label = tk.Label(frame_controles, text="Función v(t):")
v_t_label.pack()

# Botón para limpiar los campos y el gráfico
clear_button = tk.Button(root, text="Reiniciar", command=limpiar_campos)
clear_button.pack(anchor=tk.SE, padx=20, pady=20)

# Variable global para el canvas del gráfico
canvas = None

# Ejecutar la aplicación
root.mainloop()