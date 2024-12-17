
2
3
4
5
6
7
8
9
10
11
12
13
14
#Código Python - Triángulo de Pitágoras
def es_triangulo_pitagoras(a, b, c):
    lados = [a, b, c]
    lados.sort()  # Ordenar los lados en orden ascendente
    return lados[0]**2 + lados[1]**2 == lados[2]**2
 
a = float(input("Ingrese el primer lado: "))
b = float(input("Ingrese el segundo lado: "))
c = float(input("Ingrese el tercer lado: "))
 #Imprimira si es un triangulo o no de pitagoras 
if es_triangulo_pitagoras(a, b, c):
    print("¡Es un triángulo de Pitágoras!")
else:
    print("No es un triángulo de Pitágoras.")
