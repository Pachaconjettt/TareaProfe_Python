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
promocionEntradas = int(input("Hay promocion entrada?  1(SI) 0(NO)"))
valoracionPelicula = float(input("Digite la valoracion de la pelicula :"))

