°# Juego del orcado con palabras de programacion
import random

def elegir_palabra():
    palabras = ["python", "programacion", "juego", "tecnologia", "desarrollo"]
    return random.choice(palabras)

def mostrar_palabra(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def jugar_ahorcado():
    print("\n--- Bienvenido al Juego de Ahorcado ---")
    palabra = elegir_palabra()
    intentos = 6
    letras_adivinadas = set()
    letras_erradas = set()

    while intentos > 0:
        print(f"\nPalabra: {mostrar_palabra(palabra, letras_adivinadas)}")
        print(f"Intentos restantes: {intentos}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        letra = input("Adivina una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue

        if letra in letras_adivinadas or letra in letras_erradas:
            print("Ya has intentado esa letra. Intenta otra.")
            continue

        if letra in palabra:
            letras_adivinadas.add(letra)
            print("¡Correcto!")
        else:
            letras_erradas.add(letra)
            intentos -= 1
            print("Letra incorrecta.")

        if all(letra in letras_adivinadas for letra in palabra):
            print(f"\n¡Felicidades! Adivinaste la palabra: {palabra}")
            break
    else:
        print(f"\nPerdiste. La palabra era: {palabra}")

jugar_ahorcado()
