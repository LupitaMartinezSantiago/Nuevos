import random
import string

def generar_contraseña(longitud):
    if longitud < 6:
        print("La contraseña debe tener al menos 6 caracteres.")
        return

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    print(f"Contraseña generada: {contraseña}")

while True:
    print("\n--- Generador de Contraseñas ---")
    try:
        longitud = int(input("Longitud de la contraseña (0 para salir): "))
        if longitud == 0:
            print("Saliendo del generador...")
            break
        generar_contraseña(longitud)
    except ValueError:
        print("Por favor, ingresa un número válido.")
