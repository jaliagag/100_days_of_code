import time

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
            print("ok")
            c = input("¿Desea ingresar más dinero? (s / n) ")
            if c == "s":
                a = 0
            elif c == "n":
                a = 1

