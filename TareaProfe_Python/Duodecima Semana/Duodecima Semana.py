import os
import math
import numpy as np
print("\t\t Duodecima Semana y ultima :O \t\t\n")
input("Toque una tecla para continuar con los ejercicios....")
os.system("cls")

print("\t\t Primer ejercicio \t\t\n")


def PasoPorValor(pvalor):
    pvalor *= 10
    print("Dentro de una funcion", pvalor)
    return pvalor

valor = 10
valor = PasoPorValor(valor)
print("Fuera de la funcion", valor)
valor = 100
valor = PasoPorValor(valor)
print("Fuera de la funcion", valor)

input("Toque una tecla para continuar con los ejercicios....")
os.system("cls")

print("\t\t Segundo ejercicio \t\t\n")

def calcular_area_cuadrado(pvalor):
    pvalor = math.pow(pvalor,2)
    return pvalor

numero = 25
resultado = 0
print(f"Valor inicial del numero : {numero}")
resultado =  calcular_area_cuadrado(numero)
print (f"Valor final del numero : {numero}")
print(f"Resultado de la operación: {resultado}")

input("Toque una tecla pra continuar con los ejercicios....")
os.system("cls")

print("\t\t Tercer Ejercicio \t\t\n")

#Mismo ejercicio que el pasado

def calcular_area_cuadrados(pvalores):
    i = 0
    tamanno = len(pvalores)
    while(i < tamanno):
        pvalores[i] = math.pow(pvalores[i], 2)
        i += 1

def imprimir_lista(pValores):
  i = 0
  tamanno = len(pValores)
  while(i < tamanno):
      print(f"{pValores[i]}")
      i += 1

numeros = [10, 25, 85, 100]
print("\nValores iniciales de la lista :")
imprimir_lista(numeros)
print("\n\nValores finales de la lista: ")
calcular_area_cuadrados(numeros)
imprimir_lista(numeros)

input("Toque enter para seguir con los ejercicios....")
os.system("cls")

print("\t\t Cuarto Ejercicio \t\t\n")

def llenarlista(pNumeros):
    i = 0
    tamanoLista = int(input("Digite el tamano del lista: "))
    while(i < tamanoLista):
        numero = int(input(f"Digite el numero de la posicion {i + 1} : "))
        pNumeros.append(numero)
        i += 1

def calcularPromedio(pNumeros):
    i = 0
    promedio = 0
    sumaTotal = 0
    tamanno = len(pNumeros)
    while(i < tamanno):
        sumaTotal += pNumeros[i]
        i += 1
    promedio = sumaTotal / tamanno
    return promedio

numeros = []
llenarlista(numeros)
promedio = calcularPromedio(numeros);
print(f"El promedio del lista es {promedio}")

input("Toque enter para continuar....")
os.system("cls")

print("\t\t Quinto ejercicio \t\t\n")

def LlenarLista(listaNumeros):
    i = 0 
    tamanoLista = int(input("Digite el tamano del lista: "))
    while(i < tamanoLista):
        numero = int(input(f"Digite el numero de la posicion {i + 1} : "))
        listaNumeros.append(numero)
        i += 1

def contarPositivos(listaNumeros): 
    i = 0
    contPos = 0
    tamano = len(listaNumeros)
    while(i < tamano):
        if(listaNumeros[i] > 0):
            contPos += 1
        i += 1
    return contPos

def contarNegativos(listaNumeros):
    i = 0
    contNeg = 0
    tamano = len(listaNumeros)
    while(i < tamano):
        if(listaNumeros[i] < 0):
            contNeg += 1
        i += 1
    return contNeg

def contarCeros(listaNumeros):
    i = 0
    contCeros = 0
    tamano = len(listaNumeros)
    while(i < tamano):
        if(listaNumeros[i] == 0):
            contCeros += 1
        i += 1
    return contCeros

numeros = []
LlenarLista(numeros)
contPos = contarPositivos(numeros)
contNeg = contarNegativos(numeros)
contCeros = contarCeros(numeros)
print(f"Numeros positivos : {contPos}")
print(f"Numeros negativos :{contNeg}")
print(f"Ceros :{contCeros}")

input("Toque enter para seguir con los ejercicios....")
os.system("cls")

print("\t\t Sexto Ejercicio \t\t\n")

x = np.array([81,35,72,50,67,8,101,22,96,13])
print(np.amin(x))
print(np.amax(x))
print("Nuevo valor", np.insert(x,0,5)) # los pone al principio
print() 
print(np.append(x,[1,2,3])) #los pone al final

print("Valor", x[0])

def miniLista(x):
    min = x[0]
    cont = 1
    while(cont < len(x)):
        if(x[cont] < min):
            min = x[cont]
        cont += 1
    return min

def maxLista(x):
    max = x[0]
    cont = 1
    while(cont < len(x)):
        if(x[cont] > max):
            max = x[cont]
        cont += 1
    return max

input("Toque enter para seguir con el ultimo ejercicio de la semana y tambien de las semanas :,V ....")
os.system("cls")

x = np.array([81,35,72,50,67,8,101,22,96,13])
a = np.array([1,2,3,4,5,6,7,8,9])
index = [2,3,6]
new_a = np.delete(x,index)
print(new_a)

input(" ¡¡ Muchas gracias por acompañarme en estos ejercicios que me ayudaron a entender y ser mejor en python !!")
os.system("cls")