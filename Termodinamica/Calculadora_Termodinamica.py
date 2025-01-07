class CalculadoraTermodinamica:
    def __init__(self):
        pass

    def calcularCalor(self, masa, calorEsp, tempInicial, tempFinal):
        """
         q = m * c * ΔT
        """
        return masa * calorEsp * (tempFinal-tempInicial)

    def calcularMasa(self, calor, calorEsp, tempInicial, tempFinal):
        """
        m = q / (c * ΔT)

        """
        return calor / (calorEsp * (tempFinal-tempInicial))

    def calcularCalorEspecifico(self, calor, masa, tempInicial, tempFinal):
        """
        c = q / (m * ΔT)
        """
        return calor / (masa * (tempFinal-tempInicial))

    def calcularCambioTemperatura(self, calor, masa, calorEsp):
        """
        ΔT = q / (m * c)
        """
        return calor / (masa * calorEsp)

#Creo la instancia
calculadora = CalculadoraTermodinamica()

# Ejemplos..
calculosEjemplo = [
    calculadora.calcularCalor(10, 4.18,50,25), 
    calculadora.calcularMasa(1000, 4.18, 50,25), 
    calculadora.calcularCalorEspecifico(1000, 10, 50,25),
    calculadora.calcularCambioTemperatura(1000, 10, 4.18),  
    calculadora.calcularCalor(5, 2.5, 60,30),
    calculadora.calcularMasa(500, 2.5, 60,30), 
    calculadora.calcularCalorEspecifico(500, 5, 60,30),  
    calculadora.calcularCambioTemperatura(500, 5, 2.5),  
    calculadora.calcularCalor(8, 3.5, 40,20),  
    calculadora.calcularMasa(800, 3.5,40,20)   
    ]

# Print results of calculations
for i, result in enumerate(calculosEjemplo):
    print(f"Calculation {i+1}: {result}")