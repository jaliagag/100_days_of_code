import time
from vars import y

def realizarTransferencia(n):
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
        c = input("¿A quién quiere transferir? (ingrese el alias o el CBUde la cuenta" )
        print("Procesando la operación...")
        time.sleep(1)
        realizarTransferencia(b)
        c = input("¿Desea realizar otra transferencia? (s / n) ")
        if c == "s":
            a = 0
        elif c == "n":
            a = 1
