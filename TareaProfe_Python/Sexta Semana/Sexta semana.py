﻿import os
import numpy
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

input("Toquee una tecla para continuar...")
os.system("cls")

print("\t\t Septimo Ejercicio \t\t\n")

APROBACION = 70.0
AMPLIACION = 60.0
cont = 1
suma = num_examenes = nota_examen = promedio = 0.0
num_examenes = int(input("Por favor indique el numero de examenes del curso :"))

while(cont <= num_examenes):
    nota_examen = float(input("Por favor indique la nota del examen " + str(cont) + ": "))
    suma += nota_examen
    cont += 1
promedio = suma / num_examenes

if(promedio >= APROBACION):
    print("¡¡¡El estudiante aprobo!!!")
elif(promedio >= AMPLIACION):
    print("El estudiante tiene derecho a una ampliacion.")
else: 
    print("El estudiante se quedo :V ")


input("Toque una tecla para continuar..")
os.system("cls")

print("\t\t Octavo ejercicio \t\t\n")

def cal_pop_fitness(equation_inputs, pop):
    fitness = numpy.sum(pop * equation_inputs, axis = 1)
    return fitness

def select_mating_pool(pop,fitness,num_parents):
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parents_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parents_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents

def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range (offspring_size[0]):
        parent1_idx = k%parents.shape[0]
        parent2_idx = (k+1)%parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx,0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover, num_mutations = 1):
    mutations_counter = numpy.uint8(offspring_crossover.shape[1] / num_mutations)
    for idx in range(offspring_crossover.shape[0]):
        gene_idx = mutations_counter - 1
        for mutation_num in range(num_mutations):
            random_value = numpy.random.uniform(-1.0, 1.0, 1)
            offspring_crossover[idx, gene_idx] = offspring_crossover[idx, gene_idx] + random_value
            gene_idx = gene_idx + mutations_counter

    return offspring_crossover

