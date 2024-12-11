import os
import math
import numpy as np

def capturaTemperaturas(temperaturas):
    N = int(input("Digite la cantidad de temperaturas: "))
    for indice in range(N):
        temperatura = float(input(f"Digite la temperatura {indice + 1}: "))
        temperaturas.append(temperatura)

def promedioTemperaturas(temperaturas):
    suma_total = 0.0
    promedio = 0.0
    tam = len(temperaturas)
    for i in range(tam):
        suma_total += temperaturas[i]
    promedio = suma_total / tam
    print(f"El promedio de las temperaturas de la semana es: {promedio}")

def mostrarTemperaturas(temperaturas):
    i = 0
    while i < len(temperaturas):
        print(temperaturas[i])
        i += 1

def reverTemperaturas(temperaturas):
    tam = len(temperaturas) - 1
    while tam >= 0:
        print(temperaturas[tam])
        tam -= 1

def Palind(palabra):
    pal = True
    i = 0
    j = len(palabra) - 1
    while i <= j and pal:
        if palabra[i] == "*":
            i += 1
        elif palabra[j] == "*":
            j -= 1
        elif palabra[i] != palabra[j]:
            pal = False
        else:
            i += 1
            j -= 1
    return pal

alfabetoMin = "abcd"
alfabetoMay = "ABCD"

def Mayuscula(cadena, pos):
    i = 0
    while (i < len(alfabetoMin)):
        if (cadena[pos] == alfabetoMin[i]):
            cadena = cadena[:pos] + alfabetoMay[i] + cadena[pos + 1:]
        i += 1
    return cadena

def Minuscula(cadena, pos):
    i = 0
    while i < len(alfabetoMin):
        if cadena[pos] == alfabetoMay[i]:
            cadena = cadena[:pos] + alfabetoMin[i] + cadena[pos + 1:]
        i += 1
    return cadena

def convertirAmayuscula(cadena):
    for i in range(len(cadena)):
        cadena = Mayuscula(cadena, i)
    return cadena

def convertirAminuscula(cadena):
    for i in range(len(cadena)):
        cadena = Minuscula(cadena, i)
    return cadena

def main():
    temperaturas = []
    
    cadena = "arroz"
    cadena = convertirAmayuscula(cadena)
    print(cadena)
    cadena = convertirAminuscula(cadena)
    print(cadena)
    palabra = "ARRIBA*LA*BIRRA"
    pal = Palind(palabra)
    if pal:
        print("Es palind")
    else:
        print("No Es palind")
    capturaTemperaturas(temperaturas)
    print("En orden")
    mostrarTemperaturas(temperaturas)
    print("Invertido")
    reverTemperaturas(temperaturas)

main()

#NOTA DEL EDITOR, el metodo convertir may y min solo sirven si es de alguna letra que sale en la cadena ejemplo vemos en este caso 
#arroz, a la hora de compilar solo haria el Arroz sin más no haria algo extra para poner todo mayuscula, tengo que ver alguna forma como hacer eso en otro proyecto

input("\nToque una tecla para continuar con los ejercicios.....")
os.system("cls")

print("\t\t Segundo Ejercicio \t\t\n")

v = len(np.array([2,3,1,0]))
print(v)

input("¡¡¡ Muchas gracias por acompañarme en esta semana !!!")
os.system("cls")