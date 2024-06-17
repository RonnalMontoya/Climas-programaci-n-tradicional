def ingresar_temperaturas():
    """
    Función para ingresar las temperaturas diarias.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico.")
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio semanal de temperaturas.
    Retorna el promedio de la lista de temperaturas ingresadas.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

def main():
    """
    Función principal que organiza el flujo del programa.
    """
    print("Programa para calcular el promedio semanal de temperaturas.")
    
    # Ingresar las temperaturas diarias
    temperaturas = ingresar_temperaturas()
    
    # Calcular el promedio semanal
    promedio_semanal = calcular_promedio(temperaturas)
    
    # Mostrar el resultado
    print(f"Las temperaturas ingresadas son: {temperaturas}")
    print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f}°C")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
