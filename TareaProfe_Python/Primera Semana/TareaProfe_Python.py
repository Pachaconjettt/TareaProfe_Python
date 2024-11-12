import datetime
# Primer Ejercicio
costo_metro = 0.0; 
ancho = 20.0;
largo = 150.0; 
area = 0.0; 
monto = 0.0; 

costo_metro = float(input('Ingrese el costo del metro : '))

area = ancho * largo; 
monto = area * costo_metro; 

print('El monto a pagar es de: ', monto); 

#Segundo Ejercicio
fecha_actual = datetime.datetime.now(); 
print(fecha_actual); 

#Tercer Ejercicio 
#declaracion de variables 
primer_numero = 0; 
segundo_numero = 0; 

primer_numero = int(input("Digite el primer número :"))
segundo_numero = int(input("Digite el segundo número :"))

if primer_numero == segundo_numero: 
    print("Ambos números son iguales")
else: 
    if primer_numero > segundo_numero: 
        print("El número mayor es: ", primer_numero) 
    else: 
        print("El número mayor es: ", segundo_numero)

#Cuarto ejercicio 
nombre = input("Ingrese su nombre: ")
print("Hola su nombre es: ", nombre)
print("\n")
#Quinto Ejercicio

OtroNombre = " "
edad = 0
estatura =  0.0 

OtroNombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
estatura =  float(input("Ingrese su estatura: "))
print("\n")
print("El nombre es: ",OtroNombre)
print("La edad es: ", edad)
print("La estatura es: ", estatura)
#Sexto Ejercicio

pasoCurso  = bool(input("Ingrese su estado del curso (1: si Paso, 0: No paso) : "))
if pasoCurso == True:
    print("Paso el curso")
else: 
    print("No paso el curso")