import os
input("Bienvenido a la sexta semana de los ejercicios de JD....")
os.system("cls")
input("Toquee una tecla para empezar con los ejercicios.....")

os.system("cls")
print("\t\t Primer Ejercicio \t\t\n")

cantNumeros = 0 
numero = 0
sumaTotal = 0
promedio = 0
contNumeros = 1

cantNumeros = int(input("Digite la cantidad de numeros que desea ingresar :"))
while(contNumeros <= cantNumeros):
    numero = int(input("Digite el numero :"))
    sumaTotal += numero
    contNumeros += 1

print("El promedio es:", sumaTotal / cantNumeros)

input("Teclee una tecla para continuar...")
os.system("cls")

print("\t\t Segundo Ejercicio \t\t\n")

cantNumerosv2 = 0
num = 0
sumTotal = 0
promedio = 0
contNums = 1
bandera = True
respuesta = " "

while(bandera):
    num = int(input("Digite el numero :"))
    sumTotal += num
    respuesta = input("Desea continuar (S)-(N) :")
    cantNumerosv2 += 1
    if(respuesta == "N" or respuesta == "n"):
        bandera = False

print("El promedio es :", sumTotal / cantNumerosv2)
           