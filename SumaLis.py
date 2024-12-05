# Retornar la suma de los elementos impares de una lista.
 
import random
 
def sumar_impares_lista(lista):
    suma = 0
    for num in lista:
        if num % 2 != 0:
            suma += num
 
    return suma
 
def imprimir_lista(lista, nombre):
    for i, num in enumerate(lista):
        print(f"{nombre}[{i}] = {num}")
 
def leer_lista():
    lista = []
 
    i = 0
    while i < 5:
        lista.append(random.randint(0, 5))
        i += 1
    return lista
 
A = leer_lista()
imprimir_lista(A, "A")
print("Suma =", sumar_impares_lista(A))
 
import random
 
def sumar_impares_lista(lista):
    suma = 0
    for num in lista:
        if num % 2 != 0:
            suma += num
 
    return suma
 
def imprimir_lista(lista, nombre):
    for i, num in enumerate(lista):
        print(f"{nombre}[{i}] = {num}")
 
def leer_lista():
    lista = []
 
    i = 0
    while i < 5:
        lista.append(random.randint(0, 5))
        i += 1
    return lista
 
A = leer_lista()
imprimir_lista(A, "A")
print("Suma =", sumar_impares_lista(A))
