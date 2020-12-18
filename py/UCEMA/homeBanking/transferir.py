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

    recep = open(a, "r")
    valueRecep = recep.read()
    recep.close()

    recep = open(a, "w+")
    addR = int(valueRecep) + int(n)
    recep.write(str(addR))
    recep.close()

    print("Depósito realizado con éxito")
    file = open(y, "r")
    finalV = file.read()
    file.close()
    print("Saldo disponible", finalV)

def transf():
    a = 0
    while a == 0:
        file = open(y, "r")
        value = file.read()
        file.close()
        b = int(input("¿Cuánta dinero quiere transferir? "))
        if int(b) > 5000:
            print("Error: el monto máximo para realizar transferencias es de 5000 pesos por operación.")
            a = 0
        elif int(b) > int(value):
            print("Saldo insuficiente - usted cuenta con", value, "pesos en su cuenta")
            a = 0
        else:
            c = input("¿A quién quiere transferir? (ingrese el nombre de la cuenta) " )
            check = os.path.isfile(c)
            if check == True:
                print("Está seguro de que desea transferir", b, "a la cuenta", c,"? (s / n)")
                finalCheck = input()
                if finalCheck == "s":
                    print("Procesando la operación...")
                    time.sleep(1)
                    realizarTransferencia(b, c)
                elif finalCheck == "n":
                    print("Cancelando la operación...")
            else:
                print("Error: no pudimos encontrar la cuenta", c)
                a = 0

        # EXIT
        d = input("¿Desea realizar otra operación? (s / n) ")
        if d == "s":
            a = 0
        elif d == "n":
            a = 1
            
