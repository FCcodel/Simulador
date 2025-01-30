import tkinter as tk
from tkinter import ttk
import math
from PIL import Image, ImageTk 

class CalculadoraTermodinamica:
    def __init__(self):
        pass

    def calcularCalor(self, masa, calorEsp, tempInicial, tempFinal):
        """
         q = m * c * ΔT
        """
        resultado = round(masa * calorEsp * (tempFinal - tempInicial),3)
        return f"{resultado} J"

    def calcularMasa(self, calor, calorEsp, tempInicial, tempFinal):
        """
        m = q / (c * ΔT)
        """
        resultado = round(calor / (calorEsp * (tempFinal - tempInicial)),3)
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
        Longitud final = alfa * LongitudInicial * (TemperaturaFinal - TemperaturaInicial) + longitudInicial
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

    def calcularVolumenFinal(self, volumenInicial, tempInicial, tempFinal, material):
        """
        Volumen final = Beta * VolumenInicial * (TemperaturaFinal - TemperaturaInicial) + VolumenInicial
        """
        beta_dict = {
            "Alcohol Etílico": 1.12e-4,
            "Benceno": 1.24e-4,
            "Acetona": 1.5e-4,
            "Glicerina": 4.85e-4,
            "Mercurio": 1.82e-4,
            "Trementina": 9.0e-4,
            "Gasolina": 9.6e-4,
            "Aire a 0°C": 3.67e-4,
            "Helio": 3.665e-4
        }
        beta = beta_dict.get(material, 1.12e-4)  # Valor por defecto es el del Alcohol Etílico
        deltaT = tempFinal - tempInicial
        volumenFinal = beta * volumenInicial * deltaT + volumenInicial
        return f"{volumenFinal:,} cm³"  # Formatear el resultado con miles

    def calcularTrabajoIsobarico(self, presion, volumenInicial, volumenFinal):
        """
        W = -P * (Vf - Vi)
        """
        resultado = round (-presion * (volumenFinal - volumenInicial),2)
        return f"{resultado} J"
    
    def calcularTrabajoIsotermicoGases(self, masa, Temperatura, volumenInicial=None, volumenFinal=None, LongitudInicial=None, LongitudFinal=None, gasIdeal="Hidrógeno"):
        """
        sólidos y líquidos
        W = n*R*T*ln(VolumenInicial/VolumenFinal)
        Masa Molar = g/mol
        n= masa(g)/Masa molar(g/mol) --> moles.
        R: Constante universal de los gases ideales 8.314 J/(mol·K))
        """
        masaMolar_dict = {
            "Hidrógeno": 2,
            "Helio": 4,
            "Nitrógeno": 28,
            "Oxígeno": 32,
            "Neón": 20,
            "Argón": 40,
            "Dióxido de carbono": 44,
            "Metano": 16
        }
        
        # Calcular el número de moles
        masaMolar = masaMolar_dict.get(gasIdeal, 2)  # Valor por defecto es el del Hidrógeno
        n = masa / masaMolar
        
        # Constante universal de los gases ideales
        R = 8.314
        
        # Calcular el trabajo
        if volumenInicial is not None and volumenFinal is not None:
            deltaV = volumenFinal / volumenInicial
            Trabajo = n * R * Temperatura * math.log(deltaV)
        elif LongitudInicial is not None and LongitudFinal is not None:
            deltaL = LongitudFinal / LongitudInicial
            Trabajo = n * R * Temperatura * math.log(deltaL)
        else:
            raise ValueError("Debe proporcionar Volumen Inicial y Final o Longitud Inicial y Final.")
        
        return f"{Trabajo:,} J"  # Formatear el resultado con miles

    def calcularEnergiaInterna(self, masa, tempInicial, tempFinal, gasIdeal="Helio"):
        """
        ΔU = (3/2) * n * R * ΔT  --> gases monoatómicos con presión constante y volumen constante 
        """
        masaMolar_dict = {
            "Hidrógeno": 2,
            "Helio": 4,
            "Nitrógeno": 28,
            "Oxígeno": 32,
            "Neón": 20,
            "Argón": 40,
            "Dióxido de carbono": 44,
            "Metano": 16
        }
        masaMolar = masaMolar_dict.get(gasIdeal, 2)  # Valor por defecto es el del Helio
        n = masa / masaMolar
        R = 8.314
        deltaT = tempFinal - tempInicial
        energiaInterna = (3/2) * n * R * deltaT
        return f"{energiaInterna:,} J"

    def calcularPresionGasIdeal(self, volumen, temperatura, masa, gasIdeal="Hidrógeno"):
        """
        La presión en este contexto nos indica la fuerza que el gas ejerce sobre las paredes del recipiente que lo contiene
        P = (n * R * T) / V
        """
        masaMolar_dict = {
            "Hidrógeno": 2,
            "Helio": 4,
            "Nitrógeno": 28,
            "Oxígeno": 32,
            "Neón": 20,
            "Argón": 40,
            "Dióxido de carbono": 44,
            "Metano": 16,
            "Criptón": 83.798
        }
        masaMolar = masaMolar_dict.get(gasIdeal, 2)  # Valor por defecto es el del Hidrógeno
        n = masa / masaMolar
        R = 8.314
        presion = (n * R * temperatura) / volumen
        return f"{presion:,} Pa"

# función que actualiza los labels en función de las opciones.

def update_labels(event):
    # Ocultar todos los widgets primero
    label1.grid_remove()
    entry1.grid_remove()
    label2.grid_remove()
    entry2.grid_remove()
    label3.grid_remove()
    entry3.grid_remove()
    label4.grid_remove()
    entry4.grid_remove()
    label5.grid_remove()
    entry5.grid_remove()
    label6.grid_remove()
    entry6.grid_remove()
    label7.grid_remove()
    entry7.grid_remove()
    label8.grid_remove()
    entry8.grid_remove()

    opcionElegida = OpcionesCalculadora.get()
    if opcionElegida == "Calcular Calor":
        label1.config(text="Masa (kg):")
        label2.config(text="Calor Específico (J/kg °C):")
        label3.config(text="Temperatura Inicial (°C):")
        label4.config(text="Temperatura Final (°C):")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()
        label4.grid()
        entry4.grid()

    elif opcionElegida == "Calcular Masa":
        label1.config(text="Calor (J):")
        label2.config(text="Calor Específico (J/kg °C):")
        label3.config(text="Temperatura Inicial (°C):")
        label4.config(text="Temperatura Final (°C):")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()
        label4.grid()
        entry4.grid()

    elif opcionElegida == "Calcular Calor Especifico":
        label1.config(text="Calor (J):")
        label2.config(text="Masa (kg):")
        label3.config(text="Temperatura Inicial (°C):")
        label4.config(text="Temperatura Final (°C):")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()
        label4.grid()
        entry4.grid()

    elif opcionElegida == "Calcular Cambio de Temperatura":
        label1.config(text="Calor (J):")
        label2.config(text="Masa (kg):")
        label3.config(text="Calor Específico (J/kg °C):")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()

    elif opcionElegida == "Calcular Longitud Final en Expansión Térmica en Solidos":
        label1.config(text="Longitud Inicial (m):")
        label2.config(text="Temperatura Inicial (°C):")
        label3.config(text="Temperatura Final (°C):")
        label7.config(text="Material:")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()
        label7.grid()
        entry7.grid()
        entry7.config(state='readonly')
        entry7['values'] = ["Aluminio", "Latón y bronce", "Cobre", "Vidrio", "Plomo", "Acero", "Concreto"]

    elif opcionElegida == "Calcular Volumen Final en Expansión Volumétrica en Liquidos y Gases":
        label1.config(text="Volumen Inicial (cm³):")
        label2.config(text="Temperatura Inicial (°C):")
        label3.config(text="Temperatura Final (°C):")
        label7.config(text="Material:")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()
        label7.grid()
        entry7.grid()
        entry7.config(state='readonly')
        entry7['values'] = ["Alcohol Etílico", "Benceno", "Acetona", "Glicerina", "Mercurio", "Trementina", "Gasolina", "Aire a 0°C", "Helio"]

    elif opcionElegida == "Calcular Trabajo Consumido en Proceso Isobárico":
        label1.config(text="Presión (Pa):")
        label2.config(text="Volumen Inicial (m³):")
        label3.config(text="Volumen Final (m³):")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()

    elif opcionElegida == "Calcular Trabajo consumido en proceso de expansión isotérmica de un gas ideal":
        label1.config(text="Masa(m):")
        label2.config(text="Temperatura (°K):")
        label3.config(text="Volumen Inicial (m³):")
        label4.config(text="Volumen Final (m³):")
        label5.config(text="Longitud Incial (m):")
        label6.config(text="Longitud Final (m):")
        label8.config(text="Gas Ideal:")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()
        label4.grid()
        entry4.grid()
        label5.grid()
        entry5.grid()
        label6.grid()
        entry6.grid()
        label8.grid()
        entry8.grid()
        entry8.config(state='readonly')
        entry8['values'] = ["Hidrógeno", "Helio", "Nitrógeno", "Oxígeno", "Neón", "Argón", "Dióxido de Carbono", "Metano"]

    elif opcionElegida == "Calcular Energía Interna de un Gas Ideal Monoatómico":
        label1.config(text="Masa(m):")
        label2.config(text="Temperatura Inicial (°K):")
        label3.config(text="Temperatura Final (°K):")
        label8.config(text="Gas Monoatómico:")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()
        label8.grid()
        entry8.grid()
        entry8.config(state='readonly')
        entry8['values'] = ["Helio", "Neón", "Argón", "Criptón", "Xenón", "Radón", "Oganesón"]

    elif opcionElegida == "Calcular Presion de un Gas Ideal":
            label1.config(text="Volumen(m³):")
            label2.config(text="Temperatura(°K):")
            label3.config(text="masa(g):")
            label8.config(text="Gas Ideal:")
            label1.grid()
            entry1.grid()
            label2.grid()
            entry2.grid()
            label3.grid()
            entry3.grid()
            label8.grid()
            entry8.grid()
            entry8.config(state='readonly')
            entry8['values'] = ["Hidrógeno", "Helio", "Nitrógeno", "Oxígeno", "Neón", "Argón", "Dióxido de Carbono", "Metano"]

    else:
        label1.config(text="Valor 1:")
        label2.config(text="Valor 2:")
        label3.config(text="Valor 3:")
        label4.config(text="Valor 4:")
        label1.grid()
        entry1.grid()
        label2.grid()
        entry2.grid()
        label3.grid()
        entry3.grid()
        label4.grid()
        entry4.grid()
        
# Función para tomar los valores ingresados y llamar a los metodos correspondientes
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
        
        elif option == "Calcular Longitud Final en Expansión Térmica en Solidos":
            longitudInicial = float(entry1.get())
            tempInicial = float(entry2.get())
            tempFinal = float(entry3.get())
            material = entry5.get()
            result = calculadora.calcularLongitudFinal(longitudInicial, tempInicial, tempFinal, material)
        
        elif option == "Calcular Volumen Final en Expansión Volumétrica en Liquidos y Gases":
            volumenInicial = float(entry1.get())
            tempInicial = float(entry2.get())
            tempFinal = float(entry3.get())
            material = entry5.get()
            result = calculadora.calcularVolumenFinal(volumenInicial, tempInicial, tempFinal, material)

        elif option == "Calcular Trabajo Consumido en Proceso Isobárico":
            Presion = float(entry1.get())
            volumenInicial = float(entry2.get())
            volumenFinal = float(entry3.get())
            result = calculadora.calcularTrabajoIsobarico(Presion, volumenInicial, volumenFinal)

        elif option == "Calcular Trabajo consumido en proceso de expansión isotérmica de un gas ideal":
            masa = float(entry1.get())
            Temperatura = float(entry2.get())
            volumenInicial = float(entry3.get())
            volumenFinal = float(entry4.get())
            longitudInicial = float(entry5.get())
            longitudFinal = float(entry6.get())
            gasIdeal = entry8.get()
            result = calculadora.calcularTrabajoIsotermicoGases(masa,Temperatura, volumenInicial, volumenFinal,longitudInicial,longitudFinal,gasIdeal)

        elif option == "Calcular Energía Interna de un Gas Ideal Monoatómico":
            masa = float(entry1.get())
            TemperaturaInicial = float(entry2.get())
            TemperaturaFinal = float(entry3.get())
            gasIdeal = entry8.get()
            result = calculadora.calcularEnergiaInterna(masa,TemperaturaInicial,TemperaturaFinal,gasIdeal)    
        
        elif option == "Calcular Presion de un Gas Ideal":
            Volumen = float(entry1.get())
            Temperatura = float(entry2.get())
            masa = float(entry3.get())
            gasIdeal = entry8.get()
            result = calculadora.calcularPresionGasIdeal(Volumen,Temperatura,masa,gasIdeal)    
            

        Resultado.config(text=f"Resultado: {result}")
    
    except ValueError:
        Resultado.config(text="Por favor ingrese valores válidos.")


# Create instance of CalculadoraTermodinamica
calculadora = CalculadoraTermodinamica()

# creo la pantalla inicial
root = tk.Tk()
root.title("Calculadora Calorimetría")

# Ajustar el tamaño de la ventana
root.geometry("580x400")

# creo que las opciones y dropdown
OpcionesCalculadora = ttk.Combobox(root, values=["Calcular Calor", "Calcular Masa", "Calcular Calor Especifico", "Calcular Cambio de Temperatura", 
"Calcular Longitud Final en Expansión Térmica en Solidos","Calcular Volumen Final en Expansión Volumétrica en Liquidos y Gases",
"Calcular Trabajo Consumido en Proceso Isobárico","Calcular Trabajo consumido en proceso de expansión isotérmica de un gas ideal",
"Calcular Energía Interna de un Gas Ideal Monoatómico","Calcular Presion de un Gas Ideal"], width=62)

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

label5 = tk.Label(root, text="Valor 5:")
label5.grid(row=6, column=0)
entry5 = tk.Entry(root)
entry5.grid(row=6, column=1)

label6 = tk.Label(root, text="Valor 6:")
label6.grid(row=7, column=0)
entry6 = tk.Entry(root)
entry6.grid(row=7, column=1)

label7 = tk.Label(root, text="Material:")
label7.grid(row=8, column=0)
entry7 = ttk.Combobox(root)
entry7.grid(row=8, column=1)
label7.grid_remove()
entry7.grid_remove()

label8 = tk.Label(root, text="Gas Ideal:")
label8.grid(row=9, column=0)
entry8 = ttk.Combobox(root)
entry8.grid(row=9, column=1)
label8.grid_remove()
entry8.grid_remove()

BotonCalcular = tk.Button(root, text="Calcular", command=Calcular, width=18)
BotonCalcular.grid(row=10, column=1, sticky='e',padx=7,pady=10)

#Resultado = tk.Label(root, text="Resultado: ")
#Resultado.grid(row=11, column=0, columnspan=2, sticky='w', padx=10)
Resultado = tk.Label(root, text="Resultado: ", font=("Helvetica", 10, "bold"), relief="solid", borderwidth=1, padx=30, pady=5)
Resultado.grid(row=11, column=0, sticky='w', padx=16)


def convertirTemperatura(value, unit):
    if unit == 'C':
        return value + 273.15  # Convertir Celsius a Kelvin
    elif unit == 'K':
        return value - 273.15  # Convertir Kelvin a Celsius

def handle_conversion(event):
    if event.widget == celsius_entry:
        try:
            celsius = float(celsius_entry.get())
            kelvin = convertirTemperatura(celsius, 'C')
            kelvin_entry.delete(0, tk.END)
            kelvin_entry.insert(0, f"{kelvin:.2f}")
        except ValueError:
            kelvin_entry.delete(0, tk.END)
    elif event.widget == kelvin_entry:
        try:
            kelvin = float(kelvin_entry.get())
            celsius = convertirTemperatura(kelvin, 'K')
            celsius_entry.delete(0, tk.END)
            celsius_entry.insert(0, f"{celsius:.2f}")
        except ValueError:
            celsius_entry.delete(0, tk.END)

# Campos de entrada para Celsius y Kelvin
conversion_label = tk.Label(root, text="Convertir Grados:")
conversion_label.grid(row=18, column=0, columnspan=3, pady=(5, 0))

celsius_label = tk.Label(root, text="°C")
celsius_label.grid(row=19, column=0, padx=(0, 2))
celsius_entry = tk.Entry(root, width=20)
celsius_entry.grid(row=20, column=0, padx=(0, 2), pady=(0, 2))

# Reemplazar el label de texto con una imagen de flecha de doble sentido
arrow_image = Image.open("double_arrow.png")  # Asegúrate de tener esta imagen en el mismo directorio
arrow_image = arrow_image.resize((20, 20), Image.Resampling.LANCZOS)
arrow_photo = ImageTk.PhotoImage(arrow_image)
arrow_label = tk.Label(root, image=arrow_photo)
arrow_label.image = arrow_photo  # Mantener una referencia a la imagen
arrow_label.grid(row=20, column=1, padx=(0, 2), pady=(0, 2))

kelvin_label = tk.Label(root, text="°K")
kelvin_label.grid(row=19, column=2, padx=(0, 2))
kelvin_entry = tk.Entry(root, width=20)
kelvin_entry.grid(row=20, column=2, padx=(0, 2), pady=(0, 2))

# Vincular eventos de cambio de texto
celsius_entry.bind("<KeyRelease>", handle_conversion)
kelvin_entry.bind("<KeyRelease>", handle_conversion)

# Run the application
root.mainloop()