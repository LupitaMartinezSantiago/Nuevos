
gastos = {}

def agregar_gasto():
    mes = input("Escribe el mes: ")
    try:
        monto = float(input("Escribe el monto del gasto: "))
        if mes in gastos:
            gastos[mes] += monto
        else:
            gastos[mes] = monto
        print("Gasto registrado.")
    except ValueError:
        print("Monto no válido.")

def ver_gastos():
    if not gastos:
        print("\nNo hay gastos registrados.")
    else:
        print("\nGastos registrados:")
        for mes, monto in gastos.items():
            print(f"{mes}: ${monto:.2f}")

def calcular_total():
    total = sum(gastos.values())
    print(f"\nEl gasto total es: ${total:.2f}")

while True:
    print("\nCalculadora de Gastos")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Calcular total")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_gasto()
    elif opcion == "2":
        ver_gastos()
    elif opcion == "3":
        calcular_total()
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
