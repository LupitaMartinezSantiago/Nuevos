# Analizador de texto
def analizar_texto():
    archivo = input("Escribe el nombre del archivo a analizar (con extensión): ")
    try:
        with open(archivo, 'r') as f:
            contenido = f.read()
        
        lineas = contenido.split("\n")
        palabras = contenido.split()
        caracteres = len(contenido)

        print("\nAnálisis del archivo:")
        print(f"Líneas: {len(lineas)}")
        print(f"Palabras: {len(palabras)}")
        print(f"Caracteres: {caracteres}")
    except FileNotFoundError:
        print("El archivo no existe.")

analizar_texto()