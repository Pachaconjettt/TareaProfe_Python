import os
import time
# FIRST EXERCISE WEEK 2 
#Calcula el precio final de cualquier producto, si se sabe que la tasa de impuesto al valor agregado es de un
#13 %. El algoritmo debe recibir el nombre del producto y el precio, y debe imprimir el nombre del producto
#y el precio final. Para los efectos del ejercicio, Todos los productos pagan impuesto

#DECLARACION  E INICIALIZACION DE VARIABLES Y CONSTANTES 
print("\t\t Primer Ejercicio \t\t")
print("\n")
precioFinalProduct = 0.0
tasaImpuesto = 0.13
nombreProduct = ""
precioProducto = 0.0

#ENTRADA DE DATOS

nombreProduct = input("Digite el nombre del producto: ")
precioProducto = float(input("Digite el precio del producto: "))

#PROCESO

precioFinalProduct = precioProducto + (precioProducto * tasaImpuesto)

#SALIDA 

print(f"El nombre del producto es: {nombreProduct} y su precio es : {precioFinalProduct} ")
# SECOND EXERCISE
print("\t\t Segundo Ejercicio \t\t")
print("\n")

nombre =  " "
estatura = 0.0 
peso = 0
msj = " "
esCliente = False
valor1 = 4
valor2 = 2
valorResultantes = 0

valorResultantes  = valor1 + valor2 #4 + 2 = 6
valorResultantes = valor1 * valor2 #4 * 2 = 8
valorResultantes = valor1 / valor2 #4 / 2 = 2, cociente
valorResultantes = valor1 % valor2 #4 % 2 = 0, residuo

nombre = input("Ingrese su nombre :")
estatura = float(input("Ingrese su estatura :"))
peso = float(input("Ingrese su peso :"))

imc = peso / pow(estatura, 2) # estatura a la 2, mismo que sale en la biblioteca de math y conio en C++
msj =  "Saludos " + nombre + "\n" + "Su Imc es de : "

print(msj)
print(imc)

#THIRD EXERCISE
print("\t\t Tercer Ejercicio \t\t")
print("\n")
nota1 = 0.0
nota2 =  0.0
nota3  = 0.0 
sumatoria = 0.0 
cantidad = 3
promedio =  0.0 

nota1 = float(input("Ingrese la primer nota al sistema :"))
nota2 = float(input("Ingrese la segunda nota al sistema :"))
nota3 = float(input("Ingrese la tercera nota al sistema :"))

sumatoria = nota1 + nota2 + nota3
promedio  = sumatoria / cantidad

print("El promedio es: ", promedio)

#Fourth Exercise 

precio1 = 7000 
precio2 = 11000
nota = 78

if nota >= 60 and nota < 70: 
    print("Vamos a repo....")
else: 
    if nota < 60:
        print("Reprobado")
    else:
        print("Aprobado")
if precio1 == precio2:
    print("Son iguales...")
print(precio1 > precio2)
print