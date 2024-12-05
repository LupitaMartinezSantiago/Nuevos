import random
 
def buscar_elemento(lista, elemento):
    for i in range(0, len(lista)):
        if lista[i] == elemento:
            return i
 
def imprimir_lista(lista, nombre):
    for i in range(0, len(lista)):
        print(nombre + "[" + str(i) + "]=" + str(lista[i]))
 
def leer_lista():
    lista = []
 
    i = 0
    while i < 10:
        lista.append(int(random.randint(0, 10)))
        i = i + 1
    return lista
 
A = leer_lista()
imprimir_lista(A, "A")
cn = int(input("Número a buscar: "))
print("A[" + str(buscar_elemento(A, cn)) + "]")
