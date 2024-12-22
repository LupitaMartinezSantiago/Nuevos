
saldo = 0

def ver_saldo():
    print(f"\nTu saldo actual es: ${saldo:.2f}")

def depositar():
    global saldo
    try:
        monto = float(input("Escribe el monto a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Has depositado ${monto:.2f}.")
        else:
            print("El monto debe ser positivo.")
    except ValueError:
        print("Monto no válido.")

def retirar():
    global saldo
    try:
        monto = float(input("Escribe el monto a retirar: "))
        if monto > 0 and monto <= saldo:
            saldo -= monto
            print(f"Has retirado ${monto:.2f}.")
        elif monto > saldo:
            print("Fondos insuficientes.")
        else:
            print("El monto debe ser positivo.")
    except ValueError:
        print("Monto no válido.")

while True:
    print("\nBanco Virtual")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        ver_saldo()
    elif opcion == "2":
        depositar()
    elif opcion == "3":
        retirar()
    elif opcion == "4":
        print("Gracias por usar el banco virtual.")
        break
    else:
        print("Opción no válida.")
