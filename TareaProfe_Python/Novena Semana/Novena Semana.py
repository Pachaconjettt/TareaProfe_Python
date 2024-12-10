import math
import os
from re import A

def calcularPerimetroCirculo(pRadio):
    perimetro = 0
    perimetro = 2 * PI * pRadio
    return perimetro

def nombreRutina(parametroFormal1):
    valor1 = 0
    valor = parametroFormal1 * 5
    return valor

def calcularAreaCirculo(pRadio):
    area = 0
    area = PI * pow(pRadio, 2)
    return area

def calcularAreaCuadrado(pLado):
    area = 0
    area = pow(pLado, 2)
    return area

def calcularAreaPerimetroCuadrado(pLado):
    perimetro  = 0
    perimetro = pLado * 4
    return perimetro


radioLote1 =  0.0
ladoLote2 = 0.0
areaLote1 = 0.0
perimetroLote1 = 0.0
areaLote1 =  0.0
areaLote2 = 0.0
perimetroLote2 = 0.0
PI = math.pi

radioLote1 = float(input("Por favor escriba el radio del Lote 1 :"))
ladoLote2 = float(input("Por favor escriba el lado del Lote 2 :"))
if(radioLote1 < 0 or ladoLote2 < 0):
    print("Por favor ingrese valores positivos.")
else:
    areaLote1 = calcularAreaCirculo(radioLote1)

    perimetroLote1 = calcularPerimetroCirculo(radioLote1)
    print(f"El area del Lote 1 es : {areaLote1}")
    areaLote2 = calcularAreaCuadrado(ladoLote2)
    perimetroLote2 = calcularAreaPerimetroCuadrado(ladoLote2)
    print(f"El area del lote 2 es : {areaLote2}")
    print(f"El perimetro del Lote 2 es : {perimetroLote2}")


input("Toque una tecla para continuar con los ejercicios....")
os.system("cls")

print("\t\t Segundo ejercicio \t\t\n")

hipotenusa =  0.0
lado1 =  0.0
lado2 = 0.0
lado1 = float(input("Por favor escriba el lado 1: "))
lado2 = float(input("Por favor escriba el lado2: "))

def calcularHipotenusa(l1,l2):
    h = 0
    h = math.sqrt(math.pow(l1,2) + math.pow(l2,2))
    return h

hipotenusa = calcularHipotenusa(lado1,lado2)
print(f"El valor de la hipotenusa es :{hipotenusa}")

input("Toque una tecla para continuar.....")
os.system("cls")

print("\t\t Tercer ejercicio \t\t\n")

palabra = ""
palabra = input("Por favor digite la palabra: ")

def Palindromo(palabra):
    Palindromo = True
    idx1 = 0
    idx2 = len(palabra)-1
    while(idx1 < len(palabra)/2 and Palindromo):
        if(palabra[idx1]!=palabra[idx2]):
            Palindromo = False
        else:
            idx1 += 1
            idx2 -= 1
    if(Palindromo):
        print("La palabra ES palindromo")
    else:
        print("La palabra NO ES palindromo")

Palindromo(palabra)

input("Toque una tecla para seguir con los ejercicios.....")
os.system("cls")

print("\t\t Cuarto ejercicio \t\t\n")

palabra = ""
def Palindromo2(palabra):
    Palindromo2 = True
    idx12 = 0
    idx22 = len(palabra)-1
    while(idx12 < len(palabra)/2 and Palindromo2):
        if(palabra[idx12]!= palabra[idx22]):
            Palindromo2 = False
        else:
            idx12 += 1
            idx22 -= 1
    return Palindromo2

Palindromo2(palabra)
if(Palindromo2):
    print("La palabra ES un palindromo")
else: 
    print("La palabra NO ES un palindromo")

print("\n\n")
input("\t\t Muchas gracias por ver los ejercicios de la semana 9 :D \t\t\n")
os.system("cls")