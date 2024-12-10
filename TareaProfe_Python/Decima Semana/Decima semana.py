import os
def mostrarMenu():
    print("------Menu------")
    print("1, Determinar si un # es par o impar")
    print("2, Determinar si una palabra es Palindromo")
    print("3, Determinar si 2 #s son amigos")
    print("4, Salir.")
    print()

def leerOpcion():
    try:
        opcion = int(input("Seleccione una opcion: "))
        print()
        return opcion
    except:
        return -1

def NumeroImpPar(numero):
    if(numero % 2 == 0):
        print("Es par...")
    else:
        print("Es impar....")

def sumaDivisoresPropios(numero): 
    suma = 0
    for i in range (1, numero):
        if(numero % i == 0):
            suma += i
    return suma
def AmigosNumber(number1, number2):
    if (sumaDivisoresPropios(number1) == number2 and sumaDivisoresPropios(number2) == number1):
        print("¡¡¡Si son numeros amigos!!!")
    else: 
        print("No son compis :,v")
    
def Palindromo(palabra):
    Palindromo = True
    idx1 = 0
    idx2 = len(palabra)-1
    while(idx1 < len(palabra)/2 and Palindromo):
        if(palabra[idx1] != palabra[idx2]):
            Palindromo = False
        else:
            idx1 += 1
            idx2 -= 1
    if(Palindromo):
        print("La palabra SI es palindromo")
    else: 
        print("La palabra NO es palindromo")

def ejecutarOpcion(opcion):
    continuar = True
    if(opcion == 1):
        numero = 0
        numero = int(input("Digite un numero para comprobar si es par o impar: "))
        NumeroImpPar(numero)

    elif(opcion == 2):
        palabra = ""
        palabra = input("Digite una palabra para comprobar si es palindromo: ")
        Palindromo(palabra)

    elif(opcion == 3):
        number1 = 0
        number1 = int(input("Digite el primer numero para ver si son amigos con el otro numero: "))
        number2 = 0
        number2 = int(input("Digite el segundo numero: "))
        AmigosNumber(number1, number2)

    elif(opcion == 4):
        continuar = False
    else:
        print("Opcion invalida")
    input("\nToque enter para seguir con el menu.....")
    os.system("cls")
    return continuar
    


#Main
continuar = True
while(continuar == True):
    mostrarMenu()
    opcion = leerOpcion()
    continuar  = ejecutarOpcion(opcion)

input("Digite enter para seguir con los ejercicios.....")
os.system("cls")

print("\t\t Segundo y ultimo ejercicio \t\t\n")

def charAt(mylist, index):
    return(mylist[index])

mylist = ["apple", "banana", "cherry"]
x = len(mylist)
print(x)

mylist2 = "Apple"

print(mylist2.index("p"))

for index in range(len(mylist2)):
    print(charAt(mylist2, index))

end = len(mylist2)-1

for index in range(len(mylist2)):
    letra = charAt(mylist2,(end))
    print(letra,end="")
    end = end-1

