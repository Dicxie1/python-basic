
def recursividad(x):
    if x == 0 or x == 1:
        return 1
    else:
        return recursividad(x - 1) + recursividad(x - 2)

print("Programa sobre secuecia fibonnaci")
n = int(input("ingrese el numero: "))
print("la secuencia fibonnaci es %d" % (recursividad(3)))