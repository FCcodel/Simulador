import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def osciladorArmonico(t, y, k, m):
    x, v = y
    dxdt = v
    dvdt = -k/m * x
    return [dxdt, dvdt]


#La función solve_ivp de la biblioteca scipy.integrate en Python 
# se utiliza para resolver ecuaciones diferenciales ordinarias (EDO) 
#solve initial value problem 
# donde dt/dy=f(t,y)
# fun: La función que define el sistema de ecuaciones 
# Debe tener la forma fun(t, y,) y devolver un array que representa dy/dt
# t_span: Una tupla (T0,Tf)que define el intervalo de integración desde el tiempo inicial 
# y0: Un array que contiene las condiciones iniciales para las variables dependientes.
# args: Tupla de argumentos adicionales que se pasan a la función fun.
#La salida de solve_ivp es un objeto que contiene la solución del sistema de ecuaciones diferenciales. Los atributos más importantes son:
# t: Los puntos de tiempo en los que se evaluó la solución.
#y: La solución del sistema en los puntos de tiempo correspondientes.
#sol: Una función que permite evaluar la solución en cualquier punto dentro del intervalo de integración.

def resolverOsciladorArmonico(PosicionInicial, VelocidadInicial, ConstanteResorteK, Masa, TiempoFinal):
    y0 = [PosicionInicial, VelocidadInicial]
    LimitesIntegracion = (0, TiempoFinal)
    FuncionSolucion = solve_ivp(osciladorArmonico, LimitesIntegracion, y0, args=(ConstanteResorteK, Masa), dense_output=True)
    return FuncionSolucion

def graficar_resultados(sol, t_final):
    t = np.linspace(0, t_final, 300)
    z = sol.sol(t)
    plt.plot(t, z[0], label='Posición (x)')
    plt.plot(t, z[1], label='Velocidad (v)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Magnitud')
    plt.title('Oscilador Armónico Simple')
    plt.legend()
    plt.grid()
    plt.show()

def obtener_valores():
    PosicionInicial = float(posicion_inicial_entry.get())
    VelocidadInicial = float(velocidad_inicial_entry.get())
    ConstanteResorteK = float(constante_resorte_entry.get())
    Masa = float(masa_entry.get())
    TiempoFinal = float(tiempo_final_entry.get())
    FuncionSolucion = resolverOsciladorArmonico(PosicionInicial, VelocidadInicial,ConstanteResorteK, Masa, TiempoFinal)
    graficar_resultados(FuncionSolucion, TiempoFinal)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulación de Oscilador Armónico Simple")

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

# Ejecutar la aplicación
root.mainloop()