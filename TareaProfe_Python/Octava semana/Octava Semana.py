from math import e
import os
print("\t\t Octava semana JD ejercicios \t\t\n")
input("Toque una tecla para empezar con los ejercicios")
os.system("cls")

print("\t\t Primer ejercicio \t\t\n")
limite = 7
print("Numeros del 1 al 7 por medio del for\n")
for numero in range(limite):
    print(numero+1)
    print("\n")

print("Numeros del 1 al 7 por medio del while\n")
numero = 0
while(numero < 7):
    print(numero+1)
    print("\n")
    numero += 1

input("Toque una tecla para continuar con los ejercicios....")
os.system("cls")

print("\t\t Segundo Ejercicio \t\t\n")

limite = 7

for numero in range(limite):
    numero = 0
    while(numero < 7):
       print(numero)
       numero += 1 
    print("-------------")

input("Toque una tecla para continuar con los ejercicios.....")
os.system("cls")

print("\t\t Tercer Ejercicio \t\t\n")
limite = int(input("Ingrese el numero deseado :"))
for numero in range(limite):
    print(f"----- Tabla del {numero}----")
    print(f"{numero} x 0 = {numero * 0}")
    print(f"{numero} x 1 = {numero * 1}")
    print(f"{numero} x 2 = {numero * 2}")
    print(f"{numero} x 3 = {numero * 3}")
    print(f"{numero} x 4 = {numero * 4}")
    print(f"{numero} x 5 = {numero * 5}")
    print(f"{numero} x 6 = {numero * 6}")
    print(f"{numero} x 7 = {numero * 7}")
    print(f"{numero} x 8 = {numero * 8}")
    print(f"{numero} x 9 = {numero * 9}")
    print(f"{numero} x 10 = {numero * 10}")
    print("------------------------------------")

limite = int(input("Ingrese el numero deseado :"))
contador = 0
while(contador < limite):
  print(f"------Tabla del {contador}-----")
  print(f"{contador} x 0 = {contador * 0}")
  print(f"{contador} x 1 = {contador * 1}")
  print(f"{contador} x 2 = {contador * 2}")
  print(f"{contador} x 3 = {contador * 3}")
  print(f"{contador} x 5 = {contador * 5}")
  print(f"{contador} x 6 = {contador * 6}")
  print(f"{contador} x 7 = {contador * 7}")
  print(f"{contador} x 8 = {contador * 8}")
  print(f"{contador} x 9 = {contador * 9}")
  print(f"{contador} x 10 = {contador * 10}")
  print("-----------------------------")
  contador += 1

limite = int(input("Ingrese el numero deseado: "))
for numero in range(limite):
    print(f"----- Tabla del {numero} -------")
    contador = 0
    while (contador < 10):
        print(f"{numero} x {contador} = {numero * contador}")
        contador += 1
    print("-----------------------------------")

input("Toque una tecla para continuar con los ejercicios....")
os.system("cls")

print("\t\t Cuarto Ejercicio \t\t\n")


N = int(input("Digite la cantidad de sucursales: "))
ventaEmpresa = 0
diasSemanas = 6

for numero in range(N):
    print("---------------------------------")
    print(f"Digite la información para la empresa {numero + 1} -----")
    contador = 0
    ventaSucursal = 0
    nombreSucursal = input(f"Digite el nombre de la sucursal :")
    while(contador < diasSemanas):
        ventaSucursal += int(input(f"Digite el valor vendido en el dia {contador + 1} :"))
        contador += 1
    ventaEmpresa += ventaSucursal
    print(f"Las ventas de la sucursal {nombreSucursal} son de {ventaSucursal} - - - - ")
    print("- - - - - - - - - - - - - - - ")
    print(f"Las ventas de la empresa son de {ventaEmpresa} - - - -")


input("Toque una tecla para continuar con los ejercicios.......")
os.system("cls")

print("\t\t Quinto Ejercicio \t\t\n")

porcentaje = 0.15
nombreDelTrabajador = ""
cantidadHorasTrabajadas = 0
salarioXHora = 0.0
annosTrabajados = 0
puntos = 0
salarioBruto =  0.0
salarioNeto = 0.0
bonificacion = 0.0
deducciones = 0.0

nombreDelTrabajador = input("Digite el nombre del trabajador :")
cantidadHorasTrabajadas = int(input("Digite la cantidad de horas trabajadas: "))
salarioXHora = int(input("Digite el salario por hora :"))
annosTrabajados = int(input("Digite los annos trabajados :"))
puntos = int(input("Digite los puntos: "))

#Salario Bruto

salarioBruto = cantidadHorasTrabajadas  * salarioXHora
if(annosTrabajados > 5 and puntos > 25):
    bonificacion = salarioBruto * (porcentaje * 2)
else:
    if(annosTrabajados>5 or puntos>25):
        bonificacion = salarioBruto  * porcentaje

#deduccion
deducciones = salarioBruto * porcentaje

#Salario neto
salarioNeto = salarioBruto-deducciones+bonificacion

print(f"El salario Bruto es de : {salarioBruto} \n La bonificacion es :{bonificacion} \n Las deducciones son : {deducciones} \n El salario neto es : {salarioNeto}")

input("\t\t ¡Muchas gracias por acompañarme en esta semana! \t\t")
os.system("cls")