import os
import time
from vars import *
from ingresar import *
from mostrar import *
from pagarServicios import *
from transferir import *
from salir import * 
from pathlib import Path

#a = "##########################"

#print(a)
#b = print("BIENVENIDO A PYBANKING")
#print(a)

#y = input("Ingrese su nombre: ")

#y

check = os.path.isfile(y)
if check == False:
    file = open(y, "x")
    file.close()
    file_size = Path(f"{y}").stat().st_size
    if file_size == 0:
        file = open(y, "w+")
        file.write("0") 
        file.close()
#    print("archivo vacío")
#else:
#    print("con cosas")

z = 0

while z == 0:
    print("""¿Qué desea hacer? 
            1) Consultar saldo disponible 
            2) Realizar un depósito (máximo de $1000 por operación) 
            3) Transferir dinero
            4) Pagar algún servicio
            5) Salir""")
    c = int(input(""))
    if c == 1:
        mostrar()
    if c == 2:
        ingresar()
    if c == 3:
        transf()
    if c == 4:
        print("4")
    if c == 5:
        #print("GRACIAS POR USAR PYBANKING - NOS VEMOS!")
        #z = 1 
        chau()
     
#if c == 1:

    
