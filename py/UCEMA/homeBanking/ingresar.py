import time
from vars import y

def depositar(n):
    file = open(y, "r")
    value = file.read()
    file.close()

    file = open(y, "w+")
    add = int(value) + int(n)
    file.write(str(add))
    file.close()

    print("Depósito realizado con éxito")
    file = open(y, "r")
    finalV = file.read()
    file.close()
    print("Saldo disponible", finalV)

def ingresar():
    a = 0
    while a == 0:
        b = int(input("¿Cuánta dinero quiere ingresar? "))
        if b > 1000:
            print("Recuerde que el máximo para ingresar plata es de $1000")
            a = 0
        else:
            print("Procesando la operación...")
            time.sleep(1)
            depositar(b)
            c = input("¿Desea ingresar más dinero? (s / n) ")
            if c == "s":
                a = 0
            elif c == "n":
                a = 1

