
def cuentaregresiva(n):
    if n == 0:
        print(n)
        return 1
    else:
        print(n)
        cuentaregresiva(n-1)

print("programa que realiza un cuenta regresiva ")
n = int(input("ingrese el valor de inicio: "))
cuentaregresiva(n)