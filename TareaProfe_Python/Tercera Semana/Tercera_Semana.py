#Primer ejercicio 
costoAutoNuevo = 0.0 
costoFinalAuto = 0.0 
porcentajeVendedor = 0.1
impuesto = 0.30 

print("\t\t Primer Ejercicio \t\t\n")
costoAutoNuevo =  int(input("Digite el costo del auto: "))
costoFinalAuto = costoAutoNuevo + (costoAutoNuevo*porcentajeVendedor) + (costoAutoNuevo*impuesto)
print(f"El costo final del auto es de : {costoFinalAuto}")

#Segundo Ejercicio
print("\t\t Segundo Ejercicio \t\t\n")
numero = 0
numero = int(input("Por favor teclee un número para saber si es impar :"))

if(numero % 2 == 0): 
    print("El numero :", numero, "es par ")
else: 
    print("El numero :", numero, "Es impar ")

#Tercer Ejercicio 
print("\t\t Tercer Ejercicio \t\t\n")
cant_noches = 0
costo_noche = 0.0 
porc_desc = 0
descuento = 0.0
subtotal_hospedaje = 0.0 
total_hospedaje = 0.0 

cant_noches =  int(input("Ingrese la cantidad de noches a hospedarse: "))
costo_noche = float(input("Ingrese el costo de la estadia por noche: "))

if(cant_noches > 4): 
    porc_desc  = 0.05
else: 
    porc_desc = 0

subtotal_hospedaje = costo_noche * cant_noches
descuento = subtotal_hospedaje * porc_desc
total_hospedaje = subtotal_hospedaje - descuento

print(f"El costo total del hospedaje es : {total_hospedaje}")

#Cuarto Ejercicio
costo = 0
dia = " "
print("\t\t Cuarto Ejercicio \t\t\n ")
costo = int(input("Ingrese el costo de la entrada: "))
dia = input("Ingrese el nombre del dia de la semana: ")
if(dia == "miercoles"): 
    costo = costo/2
print(costo)

#Quinto Ejercicio 
print(" \t\t Quinto Ejercicio \t\t ")
horas_trabajadas = 0.0
precio_hora = 0.0 
salario = 0.0
fracciones_horas_regulares = 0.0
fracciones_horas_extras = 0.0

horas_trabajadas = float(input("Por favor teclee el numero de horas trabajadas en la semana: "))
precio_hora = float(input("Por favor teclee el salario por hora: "))
if(horas_trabajadas > 40) : 
    fracciones_horas_regulares = 40*precio_hora
    fracciones_horas_extras = (horas_trabajadas - 40) * precio_hora * 1.5
    salario = fracciones_horas_regulares + fracciones_horas_extras
else: 
    salario = horas_trabajadas  * precio_hora

print("El salario semanal de la persona es : ", salario)

#Sexto Ejercicio
print("\t\t Sexto Ejercicio \t\t\n")
horasTrabajadas = 0.0
precioHora = 0.0

horasTrabajadas = int(input("Digite las horas Trabajadores:"))
precioHora = int(input("Digite el precio por Hora: "))

calculoSalario = 0.0 
if horasTrabajadas > 40: 
    horasExtras = horasTrabajadas - 40 
    pagoHoraExtra = precioHora * 1.5
    calculoSalario = 40 * precioHora + (pagoHoraExtra * horasExtras)
else: 
    calculoSalario = horasTrabajadas * precioHora

print(calculoSalario)