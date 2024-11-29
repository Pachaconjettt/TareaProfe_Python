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

input("Toque una tecla para continuar......")
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

input("Toque una tecla para continuar......")
os.system("cls")

print("\t\t Tercer Ejercicio \t\t\n")

N = 0
N = int(input("Digite el valor de N: "))

while(N >= 1): 
    print("El valor es: ", N)
    N-= 1
    count = 0
while(count <= N):
    print("El valor es :", count)
    count += 1

input("Toque una tecla para continuar.......")
os.system("cls")

print("\t\t Cuarto Ejercicio \t\t\n")

factorial = 1
number = 0
cont = 1

number = int(input("Digite el valor de N :"))
while(cont <= number ):
    factorial *= cont
    cont+= 1

print("El valor del factorial de :", number , "es :", factorial)

input("Toque una tecla para continuar con los ejercicios.....")
os.system("cls")

print("\t\t Quinto Ejercicio \t\t\n")


cont = 1
N = int(input("Digite el valor de N :"))
while(cont <= (N/2)):
    if((N % cont) == 0):
        print("Divisor :", cont)
    cont += 1 
print("Divisor :", N)

input("Toque una tecla para continuar......")
os.system("cls")

print("\t\t Sexto Ejercicio \t\t\n")

ac = 0
esPar = True
cont = 1

while(esPar):
    if(cont % 2 != 0):
       esPar = False
    else:
        cont += 1
if(esPar == False):
    print("Hubo un valor impar")

while(cont <= 10):
    print(cont)
    ac+=cont 
  
    cont+=1 

print("El valor de ac es de :", ac)

input("\t\t Septimo Ejercicio \t\t\n")

