#Cuarta semana de ejercicios de JD
import os
print("\t\t Primer Ejercicio \t\t")

edad = 0
esEstudiante = False
respEstudiante = 0 

#Entrada de datos 

respEstudiante = int(input("Digite si es estudiante o no TRUE(1) O FALSE (0) :"))
edad = int(input("Digite la edad del estudiante :"))

if (respEstudiante == 1):
    esEstudiante = True
else: 
    esEstudiante = False

if( edad >= 18 and esEstudiante == True): 
    print("Es estudiante y mayor de edad ")

elif(edad >= 18 and esEstudiante == False):
        print("Es mayor a los 18 pero no es Estudiante")

elif(edad < 18 and esEstudiante == True):
        print("Es menor de edad pero estudiante")
else: 
        print("No es ni estudiante ni mayor de edad")

input("Presione una tecla para continuar con los ejercicios....")
os.system("cls")

print("\t\t Segundo Ejercicio \t\t\n")

numCompras = 0
costoCompras = 0 
porcDesc = 0.35
numCompras = 5
costoCompras = int(input("Digite el costo de la compra : "))

numCompras += 1 

if(numCompras >= 6 and costoCompras >= 10000): 
    costoCompras = costoCompras - (costoCompras * porcDesc)

  
print("El costo de la compra es de :" , costoCompras )

input("Presione una tecla para continuar con los ejercicios....")
os.system("cls")

print("\t\t Tercer Ejercicio \t\t\n")

fechaFuncion = 0
promocionEntradas = 0
haypromo = False
valoracionPelicula = 0.0
ParaMayores = 0
haypromo = False
esMayorEdad = False

fechaFuncion = int(input("Digite la fecha de la Funcion(Dia) :"))
promocionEntradas = int(input("Hay promocion entrada?  1(SI) 0(NO) :"))
valoracionPelicula = float(input("Digite la valoracion de la pelicula :"))
ParaMayores = bool(input("Digite 1 si es para mayores de edad y 0 si no lo es :"))

if(promocionEntradas == 1): 
    haypromo = True
else: 
    haypromo = False

if(ParaMayores == 1): 
    esMayorEdad = True
else: 
    esMayorEdad = False

if(fechaFuncion > 15 or haypromo) and (valoracionPelicula > 4 or not esMayorEdad):
    print("Vamos al cine!! ")
else: 
    print("No vamos al cine :c ")

input("Toque una tecla para seguir con los ejercicios.....")
os.system("cls")

print("\t\t Cuarto Ejercicio \t\t\n")

idioma = " "
edad = 0
experiencia = 0

idioma = input("digite Ingles(i) o Portugual (p) ")
edad = int(input("Digite la edad del estudiante: "))
experiencia = int(input("Digite los años de experiencia: "))

if (((idioma  == "i" or idioma == "p") and edad > 18 and experiencia > 1)):
    print("Si califica")
else: 
    print("No califica")

input("Toque una tecla para pasar de ejercicio....")
os.system("cls")

print("\t\t Quinto Ejercicio \t\t\n")

puntuaje = 0.0 
nota = " "

puntuaje = float(input("Digite el puntuaje: "))

if(puntuaje >= 90 ): 
    nota = "A"
elif(puntuaje >= 80): 
    nota = "B"
elif(puntuaje >= 70): 
    nota = "C"
else: 
    nota = "D"

print("Nota: ", nota)

input("Toquee una tecla para seguir con el ejercicio.....")
os.system("cls")

print("\t\t Sexto Ejercicio \t\t\n")

a = 0 
b = 0 
c = 0 
a = int(input("Digite el valor de a :"))
b = int(input("Digite el valor de b :"))
c = int(input("Digite el valor de c :"))

if(a!=b and b!=c):
    if(a > b and a>c):
        print("a es el mayor ")
    else: 
        if(b > a and b > c):
            print("b es mayor ")
        else:
            print("c es mayor ")
else:
    print("Existen al menos dos numeros iguales...")

input("Toque una tecla para continuar con los ejercicios....")
os.system("cls")

print("\t\t Septimo Ejercicio \t\t\n")

TotalComprasRealizadas = 0
montoNuevaCompra = 5.0 
descuento = 0.35 
precioFinal = 0.0 

TotalComprasRealizadas = int(input("El total de las compras realizadas es :"))
montoNuevaCompra = float(input("El monto de la nueva compra es de $ "))

if(TotalComprasRealizadas >= 6) and (montoNuevaCompra >= 10000): 
    precioFinal = montoNuevaCompra - (montoNuevaCompra * descuento)

else:
    precioFinal = montoNuevaCompra

print("El precio final es de $", precioFinal)


input("Toque una tecla para continuar con los ejercicios...")
os.system("cls")

print("\t\t Octavo Ejercicio \t\t\n")

dia = 0 
mes = 0
annio = 0 

dia = int(input("Digite el dia :"))
mes = int(input("Digite el mes :"))
annio = int(input("Digite el annio :"))

if (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12) and annio == 2023:
    if mes == 2:
        if annio % 4 == 0 and (annio % 100 != 0 or annio % 400 == 0):
            if dia > 29:
                print("Fecha invalida...")
            else:
                dia += 1
                if dia > 29:
                    dia = 1
                    mes += 1
        else:
            if dia > 28:
                print("Fecha invalida...")
            else:
                dia += 1
                if dia > 28:
                    dia = 1
                    mes += 1
    elif mes in [4, 6, 9, 11]:
        if dia > 30:
            print("Fecha invalida...")
        else:
            dia += 1
            if dia > 30:
                dia = 1
                mes += 1
    else:
        if dia > 31:
            print("Fecha invalida...")
        else:
            dia += 1
            if dia > 31:
                dia = 1
                mes += 1
    if mes > 12:
        mes = 1
        annio += 1
    print(f"Dia: {dia} Mes: {mes} Annio: {annio}")
else:
    print("Fecha invalida...")