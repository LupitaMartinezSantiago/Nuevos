def contar_vocales_consonantes(texto):
    texto = texto.lower()  # Convertir el texto a minúsculas para contar sin distinción de mayúsculas/minúsculas
    vocales = "aeiou"
    consonantes = "bcdfghjklmnpqrstvwxyz"
    contador_vocales = 0
    contador_consonantes = 0
 
    for caracter in texto:
        if caracter in vocales:
            contador_vocales += 1
        elif caracter in consonantes:
            contador_consonantes += 1
 
    return contador_vocales, contador_consonantes
 
texto_input = input("Ingrese un texto: ")
vocales, consonantes = contar_vocales_consonantes(texto_input)
print("Número de vocales:", vocales)
print("Número de consonantes:", consonantes)