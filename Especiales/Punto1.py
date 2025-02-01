import sympy as sp
from sympy.abc import t, s
import tkinter as tk
from tkinter import ttk

# Función para resolver la ecuación diferencial usando Transformada de Laplace
def solve_differential_eq(eq_str):
    # Parsear la ecuación
    eq = sp.sympify(eq_str)
    
    # Aplicar Transformada de Laplace
    laplace_eq = sp.laplace_transform(eq, t, s)
    
    # Resolver la ecuación transformada
    sol = sp.solve(laplace_eq[0], s)
    
    # Aplicar Transformada Inversa de Laplace
    inverse_laplace_sol = sp.inverse_laplace_transform(sol[0], s, t)
    
    return inverse_laplace_sol

# Función para manejar el evento del botón
def on_solve():
    eq_str = eq_entry.get()
    solution = solve_differential_eq(eq_str)
    result_label.config(text=f"Solución: {solution}")

# Crear la ventana principal
root = tk.Tk()
root.title("Solución de Ecuación Diferencial de Segundo Orden")

# Crear y colocar los widgets
ttk.Label(root, text="Ingrese la ecuación diferencial:").grid(row=0, column=0, padx=10, pady=10)
eq_entry = ttk.Entry(root, width=50)
eq_entry.grid(row=0, column=1, padx=10, pady=10)

solve_button = ttk.Button(root, text="Resolver", command=on_solve)
solve_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="Solución:")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar el bucle principal
root.mainloop()