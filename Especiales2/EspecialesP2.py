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
    plt.show()

def mostrar_ecuacion_latex(ecuacion, label):
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, ecuacion, fontsize=15, ha='center', va='center')
    ax.axis('off')
    canvas = FigureCanvasTkAgg(fig, master=label)
    canvas.draw()
    canvas.get_tk_widget().pack()

def obtener_valores():
    PosicionInicial = float(posicion_inicial_entry.get())
    VelocidadInicial = float(velocidad_inicial_entry.get())
    ConstanteResorteK = float(constante_resorte_entry.get())
    Masa = float(masa_entry.get())
    TiempoFinal = float(tiempo_final_entry.get())
    
    # Calcular la frecuencia angular
    omega = np.sqrt(ConstanteResorteK / Masa)
    
    # Definir las funciones x(t) y v(t) en formato LaTeX
    x_t_func = rf"$x(t) = {PosicionInicial} \cos({omega} t) + \frac{{{VelocidadInicial}}}{{{omega}}} \sin({omega} t)$"
    v_t_func = rf"$v(t) = -{PosicionInicial} {omega} \sin({omega} t) + {VelocidadInicial} \cos({omega} t)$"
    
    # Mostrar las funciones en la interfaz gráfica
    for widget in x_t_label.winfo_children():
        widget.destroy()
    for widget in v_t_label.winfo_children():
        widget.destroy()
    mostrar_ecuacion_latex(x_t_func, x_t_label)
    mostrar_ecuacion_latex(v_t_func, v_t_label)
    
    FuncionSolucion = resolverOsciladorArmonico(PosicionInicial, VelocidadInicial, ConstanteResorteK, Masa, TiempoFinal)
    graficar_resultados(FuncionSolucion, TiempoFinal)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulación de Oscilador Armónico Simple")

# Ajustar el tamaño de la ventana
root.geometry("550x400")  # Ancho x Alto
root.minsize(400, 300)    # Tamaño mínimo
root.maxsize(800, 600)    # Tamaño máximo

# Entrada para la posición inicial
posicion_inicial_label = tk.Label(root, text="Posición Inicial (m)")
posicion_inicial_label.pack()
posicion_inicial_entry = tk.Entry(root)
posicion_inicial_entry.pack()

# Entrada para la velocidad inicial
velocidad_inicial_label = tk.Label(root, text="Velocidad Inicial (m/s)")
velocidad_inicial_label.pack()
velocidad_inicial_entry = tk.Entry(root)
velocidad_inicial_entry.pack()

# Entrada para la constante del resorte
constante_resorte_label = tk.Label(root, text="Constante del Resorte (N/m)")
constante_resorte_label.pack()
constante_resorte_entry = tk.Entry(root)
constante_resorte_entry.pack()

# Entrada para la masa
masa_label = tk.Label(root, text="Masa (kg)")
masa_label.pack()
masa_entry = tk.Entry(root)
masa_entry.pack()

# Entrada para el tiempo final
tiempo_final_label = tk.Label(root, text="Tiempo Final (s)")
tiempo_final_label.pack()
tiempo_final_entry = tk.Entry(root)
tiempo_final_entry.pack()

# Botón para obtener los valores y resolver la ecuación
submit_button = tk.Button(root, text="Resolver", command=obtener_valores)
submit_button.pack()

# Etiquetas para mostrar las funciones x(t) y v(t)
x_t_label = tk.Label(root, text="Función x(t):")
x_t_label.pack()
v_t_label = tk.Label(root, text="Función v(t):")
v_t_label.pack()

# Ejecutar la aplicación
root.mainloop()