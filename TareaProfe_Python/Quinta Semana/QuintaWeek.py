#Quinta Semana
import os
print("\t\t Primer Ejercicio \t\t")
salBase = 0.0
horasExtras = 0 
codigoDePuesto = 0
maxHorasExtras = 30
montoHorasExtra = 0

horasExtras = int(input("Ingrese las horas extras que trabaja :"))
codigoDePuesto = int(input("digite el codigo del puesto :"))

if(codigoDePuesto == 1): 
    salBase = 750000
    montoHorasExtra = 6250
elif(codigoDePuesto == 2): 
    salBase = 1300000
    montoHorasExtra = 10800
elif(codigoDePuesto == 3):
    salBase = 675000
    montoHorasExtra = 5625
elif(codigoDePuesto == 4):
    salBase = 1150000
    montoHorasExtra = 0
else:
    salBase =  0
    montoHorasExtra = 0
if(horasExtras <= maxHorasExtras):
    salTotal = salBase + (montoHorasExtra * horasExtras)
else: 
    salTotal = salBase + (maxHorasExtras * montoHorasExtra)

print("El salario total seria de :", salTotal)

input("Toquee una tecla para seguir con otro ejercicio....")
os.system("cls")
#Ejercicio 2

print("\t\t Segundo Ejercicio \t\t\n")

MAXIMO_HORAS_EXTRA = 30
codigo_puesto = 0 
cantidad_horas_extras = 0
salarioBase = 0
monto_Horas_Extras = 0
salario_Total = 0

print("------------------------------------------")
print("CALCULO DE SALARIO POR MES")
print("------------------------------------------")
print(" 1) Ingeniero Civil")
print(" 2) Ingeniero Software")
print(" 3) Ingeniero Electrico")
print(" 4) Ingeniero Industrial")
print("------------------------------------------")

codigo_puesto = int(input("Digite el codigo del puesto :"))
if(codigo_puesto == 1):
    salarioBase = 750000
    monto_Horas_Extras = 6250
elif(codigo_puesto == 2): 
    salarioBase = 1300000
    monto_Horas_Extras = 10800
elif(codigo_puesto == 3):
    salarioBase = 675000
    monto_Horas_Extras = 5625
elif(codigo_puesto == 4):
    salarioBase = 1150000
    monto_Horas_Extras = 0
else:
    salarioBase = 0
    monto_Horas_Extras = 0

if(salarioBase != 0):
    if(codigo_puesto <= 3):
        cantidad_horas_extras = int(input("Digite la cantidad de horas extras trabajadas :"))
        if(cantidad_horas_extras <= MAXIMO_HORAS_EXTRA):
            salario_Total = salarioBase + (cantidad_horas_extras * monto_Horas_Extras)
        else:
            salario_Total = salarioBase + (MAXIMO_HORAS_EXTRA * monto_Horas_Extras)
    else:
     salario_Total = salarioBase
    print(f">> El salario total del ingeniero es de :{salario_Total} colones \n")
else: 
    print("ERROR AL CALCULAR EL SALARIO. POR FAVOR VERIFIQUE EL CODIGO PUESTO. \n")

input("Toquee una tecla para terminar los ejercicios de la semana..")
os.system("cls")