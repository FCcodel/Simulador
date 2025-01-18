import tkinter as tk
from tkinter import ttk

class CalculadoraTermodinamica:
    def __init__(self):
        pass

    def calcularCalor(self, masa, calorEsp, tempInicial, tempFinal):
        """
         q = m * c * ΔT
        """
        resultado = masa * calorEsp * (tempFinal-tempInicial) 
        return f"{resultado} J"

    def calcularMasa(self, calor, calorEsp, tempInicial, tempFinal):
        """
        m = q / (c * ΔT)
        """
        resultado = calor / (calorEsp * (tempFinal-tempInicial))
        return f"{resultado} kg"

    def calcularCalorEspecifico(self, calor, masa, tempInicial, tempFinal):
        """
        c = q / (m * ΔT)
        """
        resultado  = round ((calor / (masa * (tempFinal-tempInicial))),3)
        return f"{resultado} 'J/kg.°C"

    def calcularCambioTemperatura(self, calor, masa, calorEsp):
        """
        ΔT = q / (m * c)
        """
        resultado = round (calor / (masa * calorEsp))
        return f"{resultado} °C"

# Function to update labels based on selected option
def update_labels(event):
    opcionElegida = OpcionesCalculadora.get()
    if opcionElegida == "Calcular Calor":
        label1.config(text="Masa (kg):")
        label2.config(text="Calor Específico (J/kg °C):")
        label3.config(text="Temperatura Inicial (°C):")
        label4.config(text="Temperatura Final (°C):")

    elif opcionElegida == "Calcular Masa":
        label1.config(text="Calor (J):")
        label2.config(text="Calor Específico (J/kg °C):")
        label3.config(text="Temperatura Inicial(°C):")
        label4.config(text="Temperatura Final(°C):")

    elif opcionElegida == "Calcular Calor Especifico":
        label1.config(text="Calor (J):")
        label2.config(text="Masa (kg):")
        label3.config(text="Temperatura Inicial (°C):")
        label4.config(text="Temperatura Final (°C):")

    elif opcionElegida == "Calcular Cambio de Temperatura":
        label1.config(text="Calor (J):")
        label2.config(text="Masa (kg):")
        label3.config(text="Calor Específico (J/kg °C):")
        label4.grid_remove()
        entry4.grid_remove()

    elif opcionElegida == "Proceso Isobárico":
        label1.config(text="Calor (J):")
        label2.config(text="Masa (kg):")
        label3.config(text="Calor Específico (J/kg °C):")
        label4.grid_remove()
        entry4.grid_remove()


    else:
        label1.config(text="Valor 1:")
        label2.config(text="Valor 2:")
        label3.config(text="Valor 3:")
        label4.grid()
        entry4.grid()

# Function to perform calculation based on selected option
def Calcular():
    option = OpcionesCalculadora.get()
    try:
        if option == "Calcular Calor":
            masa = float(entry1.get())
            calorEsp = float(entry2.get())
            tempInicial = float(entry3.get())
            tempFinal = float(entry4.get())
            result = calculadora.calcularCalor(masa, calorEsp, tempInicial, tempFinal)
        elif option == "Calcular Masa":
            calor = float(entry1.get())
            calorEsp = float(entry2.get())
            tempInicial = float(entry3.get())
            tempFinal = float(entry4.get())
            result = calculadora.calcularMasa(calor, calorEsp, tempInicial, tempFinal)
        elif option == "Calcular Calor Especifico":
            calor = float(entry1.get())
            masa = float(entry2.get())
            tempInicial = float(entry3.get())
            tempFinal = float(entry4.get())
            result = calculadora.calcularCalorEspecifico(calor, masa, tempInicial, tempFinal)
        elif option == "Calcular Cambio de Temperatura":
            calor = float(entry1.get())
            masa = float(entry2.get())
            calorEsp = float(entry3.get())
            result = calculadora.calcularCambioTemperatura(calor, masa, calorEsp)
        
        Resultado.config(text=f"Resultado: {result}")
    except ValueError:
        Resultado.config(text="Por favor ingrese valores válidos.")

# Create instance of CalculadoraTermodinamica
calculadora = CalculadoraTermodinamica()

# creo la pantalla inicial
root = tk.Tk()
root.title("Calculadora Termodinámica")

# creo que las opciones y dropdown
OpcionesCalculadora = ttk.Combobox(root, values=["Calcular Calor", "Calcular Masa", "Calcular Calor Especifico", "Calcular Cambio de Temperatura"])
OpcionesCalculadora.grid(row=0, column=1)
OpcionesCalculadora.set("Seleccione una opción")
OpcionesCalculadora.bind("<<ComboboxSelected>>", update_labels)

label1 = tk.Label(root, text="Valor 1:")
label1.grid(row=1, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

label2 = tk.Label(root, text="Valor 2:")
label2.grid(row=2, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

label3 = tk.Label(root, text="Valor 3:")
label3.grid(row=3, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=3, column=1)

label4 = tk.Label(root, text="Valor 4:")
label4.grid(row=4, column=0)
entry4 = tk.Entry(root)
entry4.grid(row=4, column=1)

BotonCalcular = tk.Button(root, text="Calcular", command=Calcular)
BotonCalcular.grid(row=5, columnspan=2)

Resultado = tk.Label(root, text="Resultado: ")
Resultado.grid(row=6, columnspan=2)

# Run the application
root.mainloop()
