from ingresar import *
from mostrar import *
from pagarServicios import *
from transferir import *
from salir import * 

a = "##########################"

print(a)
b = print("BIENVENIDO A PYBANKING")
print(a)

y = input("Ingrese su nombre: ")

z = 0

while z == 0:
    print("""¿Qué desea hacer? 
            1) Consultar saldo disponible 
            2) Realizar un depósito (máximo de $1000 por operación) 
            3) Transferir dineron
            4) Pagar algún servicio
            5) Salir""")
    c = int(input(""))
    if c == 1:
        print("1")
    if c == 2:
        ingresar()
    if c == 3:
        print("3")
    if c == 4:
        print("4")
    if c == 5:
        #print("GRACIAS POR USAR PYBANKING - NOS VEMOS!")
        #z = 1 
        chau()
     
#if c == 1:

    
    
