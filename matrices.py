
def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento en la posición [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz
 
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()
 
def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado
 
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
 
print("Ingrese la primera matriz:")
matriz1 = crear_matriz(filas, columnas)
 
print("Ingrese la segunda matriz:")
matriz2 = crear_matriz(filas, columnas)
 # Se imprimira la matriz
print("Matriz 1:")
imprimir_matriz(matriz1)
 
print("Matriz 2:")
imprimir_matriz(matriz2)
 
matriz_suma = sumar_matrices(matriz1, matriz2)
print("Resultado de la suma:")
imprimir_matriz(matriz_suma)
