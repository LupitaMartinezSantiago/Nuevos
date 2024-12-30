
libros = []

def agregar_libro():
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    año = input("Año de publicación: ")
    libros.append({"titulo": titulo, "autor": autor, "año": año})
    print("Libro registrado exitosamente.")
# con el titulo del libro registrado
def buscar_libro():
    titulo = input("Escribe el título del libro a buscar: ")
    encontrados = [l for l in libros if l['titulo'].lower() == titulo.lower()]
    if encontrados:
        print("\nLibros encontrados:")
        for l in encontrados:
            print(f"Título: {l['titulo']}, Autor: {l['autor']}, Año: {l['año']}")
    else:
        print("No se encontró ningún libro con ese título.")
# Mostrara los libros que esten registrados
def mostrar_libros():
    if not libros:
        print("No hay libros registrados.")
    else:
        print("\nLista de libros:")
        for l in libros:
            print(f"Título: {l['titulo']}, Autor: {l['autor']}, Año: {l['año']}")
# Obciones de  busqueda 
while True:
    print("\nGestor de Libros")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Mostrar todos los libros")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        buscar_libro()
    elif opcion == "3":
        mostrar_libros()
    elif opcion == "4":
        print("Saliendo del gestor de libros...")
        break
    else:
        print("Opción no válida.")
