import tkinter as tk
from tkinter import ttk

class CalculadoraTermodinamica:
    def __init__(self):
        pass

    def calcularCalor(self, masa, calorEsp, tempInicial, tempFinal):
        """
         q = m * c * ΔT
        """
        resultado = masa * calorEsp * (tempFinal - tempInicial)
        return f"{resultado} J"

    def calcularMasa(self, calor, calorEsp, tempInicial, tempFinal):
        """
        m = q / (c * ΔT)
        """
        resultado = calor / (calorEsp * (tempFinal - tempInicial))
        return f"{resultado} kg"

    def calcularCalorEspecifico(self, calor, masa, tempInicial, tempFinal):
        """
        c = q / (m * ΔT)
        """
        resultado = round((calor / (masa * (tempFinal - tempInicial))), 3)
        return f"{resultado} J/kg.°C"

    def calcularCambioTemperatura(self, calor, masa, calorEsp):
        """
        ΔT = q / (m * c)
        """
        resultado = round(calor / (masa * calorEsp))
        return f"{resultado} °C"

    def calcularLongitudFinal(self, longitudInicial, tempInicial, tempFinal, material):
        """
        Longitud final = alfa * LongitudInicial * (TemperaturaFinal - TemperaturaInicial)
        """
        alfa_dict = {
            "Aluminio": 24e-6,
            "Latón y bronce": 19e-6,
            "Cobre": 17e-6,
            "Vidrio": 9e-6,
            "Plomo": 29e-6,
            "Acero": 11e-6,
            "Concreto": 12e-6
        }
        alfa = alfa_dict.get(material, 11e-6)  # Valor por defecto es el del acero
        deltaT = tempFinal - tempInicial
        longitudFinal = longitudInicial + alfa * longitudInicial * deltaT
        return f"{longitudFinal:,} m"  # Formatear el resultado con miles

# Function to update labels based on selected option
def update_labels(event):
    opcionElegida = OpcionesCalculadora.get()
    if opcionElegida == "Calcular Calor":
        label1.config(text="Masa (kg):")
        label2.config(text="Calor Específico (J/kg °C):")
        label3.config(text="Temperatura Inicial (°C):")
        label4.config(text="Temperatura Final (°C):")
        label4.grid()
        entry4.grid()
        label5.grid_remove()
        entry5.grid_remove()

    elif opcionElegida == "Calcular Masa":
        label1.config(text="Calor (J):")
        label2.config(text="Calor Específico (J/kg °C):")
        label3.config(text="Temperatura Inicial (°C):")
        label4.config(text="Temperatura Final (°C):")
        label4.grid()
        entry4.grid()
        label5.grid_remove()
        entry5.grid_remove()

    elif opcionElegida == "Calcular Calor Especifico":
        label1.config(text="Calor (J):")
        label2.config(text="Masa (kg):")
        label3.config(text="Temperatura Inicial (°C):")
        label4.config(text="Temperatura Final (°C):")
        label4.grid()
        entry4.grid()
        label5.grid_remove()
        entry5.grid_remove()

    elif opcionElegida == "Calcular Cambio de Temperatura":
        label1.config(text="Calor (J):")
        label2.config(text="Masa (kg):")
        label3.config(text="Calor Específico (J/kg °C):")
        label4.grid_remove()
        entry4.grid_remove()
        label5.grid_remove()
        entry5.grid_remove()

    elif opcionElegida == "Expansión Térmica en Acero":
        label1.config(text="Longitud Inicial (m):")
        label2.config(text="Temperatura Inicial (°C):")
        label3.config(text="Temperatura Final (°C):")
        label4.grid_remove()
        entry4.grid_remove()
        label5.config(text="Material:")
        label5.grid()
        entry5.grid()
        entry5.config(state='readonly')
        entry5['values'] = ["Aluminio", "Latón y bronce", "Cobre", "Vidrio", "Plomo", "Acero", "Concreto"]

    else:
        label1.config(text="Valor 1:")
        label2.config(text="Valor 2:")
        label3.config(text="Valor 3:")
        label4.config(text="Valor 4:")
        label4.grid()
        entry4.grid()
        label5.grid_remove()
        entry5.grid_remove()

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
        
        elif option == "Expansión Térmica en Acero":
            longitudInicial = float(entry1.get())
            tempInicial = float(entry2.get())
            tempFinal = float(entry3.get())
            material = entry5.get()
            result = calculadora.calcularLongitudFinal(longitudInicial, tempInicial, tempFinal, material)
        
        Resultado.config(text=f"Resultado: {result}")
    
    except ValueError:
        Resultado.config(text="Por favor ingrese valores válidos.")

# Create instance of CalculadoraTermodinamica
calculadora = CalculadoraTermodinamica()

# creo la pantalla inicial
root = tk.Tk()
root.title("Calculadora Calorimetría")

# Ajustar el tamaño de la ventana
root.geometry("380x380")

# creo que las opciones y dropdown
OpcionesCalculadora = ttk.Combobox(root, values=["Calcular Calor", "Calcular Masa", "Calcular Calor Especifico", "Calcular Cambio de Temperatura", "Expansión Térmica en Acero"], width=40)
OpcionesCalculadora.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
OpcionesCalculadora.set("Seleccione una opción")
OpcionesCalculadora.bind("<<ComboboxSelected>>", update_labels)

# Texto explicativo
texto_explicativo = tk.Label(root, text="Ingrese los valores correspondientes en los campos a continuación:")
texto_explicativo.grid(row=1, column=0, columnspan=2)

label1 = tk.Label(root, text="Valor 1:")
label1.grid(row=2, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=2, column=1)

label2 = tk.Label(root, text="Valor 2:")
label2.grid(row=3, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=3, column=1)

label3 = tk.Label(root, text="Valor 3:")
label3.grid(row=4, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=4, column=1)

label4 = tk.Label(root, text="Valor 4:")
label4.grid(row=5, column=0)
entry4 = tk.Entry(root)
entry4.grid(row=5, column=1)

label5 = tk.Label(root, text="Material:")
label5.grid(row=6, column=0)
entry5 = ttk.Combobox(root)
entry5.grid(row=6, column=1)
label5.grid_remove()
entry5.grid_remove()

BotonCalcular = tk.Button(root, text="Calcular", command=Calcular, width=20)
BotonCalcular.grid(row=7, column=1, sticky='e', padx=10, pady=10)

Resultado = tk.Label(root, text="Resultado: ")
Resultado.grid(row=8, column=0, columnspan=2, sticky='w', padx=10)

# Run the application
root.mainloop()