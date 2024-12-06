
import os

print("\t\tSeptima semana ejercicios JD Murillo\t\t\n")
input("Toca enter para empezar con los ejercicios...\t\t\n")
os.system("cls")

print("\t\tPrimer Ejercicio\t\t\n")

Primo = True
contador1 = 1
acumulador = 0
#Este ejercicio parece que esta mal hecho por si las moscas
cantidadNumeros = int(input("Digite la cantidad de numeros: "))

while(contador1 <= cantidadNumeros):
    contador2 = 2
    acumuladorPrimo = 0

    Primo = True
    contadorPrimo = 0
    numero = int(input("Digite los numeros :"))

    while(Primo and contador2<=numero):
        if((numero % contador2) == 0):
         print("entra")
         Primo = False

        contador2 = contador2 + 1
    if(Primo):
        print("No entra")
        acumuladorPrimo += numero
        contadorPrimo += 1

    contador1 = contador1 + 1

print("Acumulador de primos :", acumuladorPrimo, "total :", contadorPrimo)
    
input("Toque una tecla para seguir con los ejercicios...")
os.system("cls")

print("\t\t Segundo Ejercicio \t\t\n")

suma_total = 0
numero = 0

numero = int(input("Digite un numero :"))
suma_total = numero

while(suma_total < 1000):
    numero = int(input("Por favor ingrese un numero :"))
    suma_total += numero 

print("El valor total de la suma es : ", suma_total)

input("Toque una tecla para seguir con los ejercicios....")
os.system("cls")

print("\t\t Tercer Ejercicio \t\t\n")

numero_secreto = 0
numero = 0
cantidad_intentos = 0

numero_secreto = int(input("Digite el numero secreto :"))

while(numero != numero_secreto):
    numero = int(input("Digite un numero :"))
    if(numero == numero_secreto):
        print(" ¡Numero correcto! ")
    else:
        if(numero > numero_secreto):
            print("Digite un numero menor ")
        else:
            print("Digite un numero mayor ")
    
    cantidad_intentos += 1

print("Total de intentos realizados :", cantidad_intentos)

input("Toque una tecla para continuar con los ejercicios......")
os.system("cls")

print("\t\t Cuarto Ejercicio \t\t\n")

band = True
N = 0
N = int(input("Digite la cantidad de usuarios :"))
for user in range(N):
    print("Para el usuario #", user+1)
    band = True
    while(band):
        numero = int(input("Digite el número :"))
        if(numero%2==0):
            print(numero)
        else:
            print("Numero no par....")
            band = not band

input("Toque una tecla para seguir con los ejercicios...")
os.system("cls")

print("\t\t Quinto Ejercicio \t\t\n")

N = 0
numFabricas = 12
nombreFabricas = [None] * numFabricas
ProduccionMensual = [0] * numFabricas
totalAnual = 0
for x in range(numFabricas):
    nombreFabricas[x] = input(f"Por favor digite el nombre fabrica {x+1} : ")
    totalAnual = 0
    FabMay = 0
    contMayor3mill = 0
    for i in range (numFabricas):
        ProduccionMensual [i] = int(input(f"Digite la produccion del mes {i+1}: "))
        totalAnual = totalAnual + ProduccionMensual[i]
    if(totalAnual > FabMay):
        FabMay = totalAnual
        posMayor = x
    if(i== 7 and ProduccionMensual[i] > 3000000):
        contMayor3mill += 1
    print(f"La fabrica {nombreFabricas[x]} tiene una produccion anual de {totalAnual}")
    print(f"La fabrica con mayor produccion es: {nombreFabricas[posMayor]}")


input("Toque una tecla para seguir con el ultimo ejercicio...")
os.system("cls")

print("\t\t Sexto Ejercicio \t\t\n")

saldo = retiro =  0
saldo = int(input("Digite el monto inicial :"))
while(saldo >= retiro): 
    retiro = int(input("Digite la cantidad de retiro : "))
    print(f"Se ha retirado.... {retiro} el saldo es de {saldo-retiro}")
    saldo -= retiro
print("Se ha quedado sin fondo....")


