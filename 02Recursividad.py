#Programa en python que calcule el factorial de  número

def factotial(x):
    if x == 1:
        return 1
    else:
        return x + factotial(x -1)

print("Progama que calcule el factoria de un número entero positivo")
numero = int (input("Ingrese un numero: "))
print("El factorial de un número es %d" % factotial(numero))
