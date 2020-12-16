import os
import time
from vars import y

def realizarTransferencia(n, a):
    # n is the amount to be transfered
    # a is the receipent account
    file = open(y, "r")
    value = file.read()
    file.close()

    file = open(y, "w+")
    subs = int(value) - int(n)
    file.write(str(subs))
    file.close()

    print("Depósito realizado con éxito")
    file = open(y, "r")
    finalV = file.read()
    file.close()
    print("Saldo disponible", finalV)

def transf():
    a = 0
    while a == 0:
        b = int(input("¿Cuánta dinero quiere transferir? "))
        c = input("¿A quién quiere transferir? (ingrese el nombre de la cuenta) " )
        check = os.path.isfile(c)
        if check == True:
            finalCheck = input("Está seguro de que desea transferir", b, "a la cuenta", c,"? (s / n)")
            if finalCheck == "s":
                print("Procesando la operación...")
                time.sleep(1)
                realizarTransferencia(b, c)
            elif finalCheck == "n":
                print("Cancelando la operación...")
            d = input("¿Desea realizar otra transferencia? (s / n) ")
            if d == "s":
                a = 0
            elif d == "n":
                a = 1
        else:
            print("Error: no pudimos encontrar la cuenta", c)
            a = 0
