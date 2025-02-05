from sympy import symbols, Function, Eq, exp, sin, laplace_transform, inverse_laplace_transform
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Definir las variables y la función
t, s = symbols('t s')
Y = Function('Y')(s)
y = Function('y')(t)

# Definir la ecuación diferencial
diffeq = Eq(y.diff(t, t) + y, exp(-2*t) * sin(t))

# Aplicar la transformada de Laplace a ambos lados de la ecuación
laplace_eq = laplace_transform(diffeq.lhs, t, s)[0] - laplace_transform(diffeq.rhs, t, s)[0]

# Sustituir las condiciones iniciales y(0)=0 y y'(0)=0
laplace_eq = laplace_eq.subs({y.subs(t, 0): 0, y.diff(t).subs(t, 0): 0})

# Resolver para Y(s)
Y_s = laplace_eq.simplify()

# Encontrar la solución inversa de Laplace para obtener y(t)
sol = inverse_laplace_transform(Y_s, s, t)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Solución de la Ecuación Diferencial")
root.geometry("800x600")  # Ajustar el tamaño de la ventana

# Crear una figura de matplotlib para mostrar las ecuaciones
fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño de la figura

# Ocultar los ejes
ax.axis('off')

# Mostrar las ecuaciones en formato LaTeX
equations = [
    r"Hallar la solución a la ecuación diferencial: $y'' + y = e^{-2t} \sin(t)$",
    r"Condiciones iniciales: $y(0)=0$, $y'(0)=0$ utilizando la transformada de Laplace.",
    r"Paso 1: Aplicamos la transformada a ambos miembros de la ecuación:",
    r"$\mathcal{L}\{y''\} + \mathcal{L}\{y\} = \mathcal{L}\{e^{-2t} \sin(t)\}$",
    r"Paso 2: Para encontrar la transformada de una derivada utilizaremos las siguientes fórmulas:",
    r"$a- \mathcal{L}\{y''\} = s^2Y(s) - sy(0) - y'(0)$",
    r"$b- \mathcal{L}\{y\} = Y(s)$",
    r"$c- \mathcal{L}\{e^{at} \sin(kt)\} = \frac{k}{(s-a)^2 + k^2}$",
    r"Paso 3: Reemplazamos en la igualdad las expresiones iniciales por las equivalencias acorde a las fórmulas del paso 2:",
    r"$s^2Y(s) - sy(0) - y'(0) + Y(s) = \frac{1}{(s+2)^2 + 1}$",
    r"Paso 4: Sustituimos las condiciones iniciales $y(0)=0$, $y'(0)=0$ :",
    f"Solución: ${sol}$"
]

# Añadir las ecuaciones a la figura
for i, eq in enumerate(equations):
    ax.text(0.1, 0.9 - i*0.08, eq, fontsize=12, verticalalignment='top')

# Crear un canvas de Tkinter para mostrar la figura
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Ejecutar la interfaz gráfica
root.mainloop()