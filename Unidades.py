# Permite calcular las unidades de medida
def convertir_longitud():
    print("\n--- Conversión de Longitud ---")
    print("1. Metros a Kilómetros")
    print("2. Metros a Millas")
    print("3. Millas a Metros")
    opcion = input("Elige una opción: ")
    try:
        valor = float(input("Ingresa el valor a convertir: "))
        if opcion == "1":
            print(f"{valor} metros = {valor / 1000} kilómetros")
        elif opcion == "2":
            print(f"{valor} metros = {valor / 1609.34:.4f} millas")
        elif opcion == "3":
            print(f"{valor} millas = {valor * 1609.34} metros")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def convertir_peso():
    print("\n--- Conversión de Peso ---")
    print("1. Kilogramos a Libras")
    print("2. Libras a Kilogramos")
    opcion = input("Elige una opción: ")
    try:
        valor = float(input("Ingresa el valor a convertir: "))
        if opcion == "1":
            print(f"{valor} kilogramos = {valor * 2.20462:.4f} libras")
        elif opcion == "2":
            print(f"{valor} libras = {valor / 2.20462:.4f} kilogramos")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def convertir_temperatura():
    print("\n--- Conversión de Temperatura ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Elige una opción: ")
    try:
        valor = float(input("Ingresa el valor a convertir: "))
        if opcion == "1":
            print(f"{valor}°C = {valor * 9/5 + 32}°F")
        elif opcion == "2":
            print(f"{valor}°F = {(valor - 32) * 5/9:.2f}°C")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

while True:
    print("\n--- Conversor de Unidades ---")
    print("1. Longitud")
    print("2. Peso")
    print("3. Temperatura")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        convertir_longitud()
    elif opcion == "2":
        convertir_peso()
    elif opcion == "3":
        convertir_temperatura()
    elif opcion == "4":
        print("Saliendo del conversor...")
        break
    else:
        print("Opción no válida.")
