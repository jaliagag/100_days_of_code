import os
from pathlib import Path


y = input('who the fuck are you? ')

check = os.path.isfile(y)
if check == False:
    file = open(y, "x")
    file.close()
    file_size = Path(f"{y}").stat().st_size
    if file_size == 0:
        file = open(y, "w+")
        file.write("0\n") 
        file.write("agenda = {}")
        file.close()
#
print("REALIZAR UNA TRANSFERENCIA") 
print("""
        1 Realizar una transferencia 
        2 Ver personas agendadas
        3 Agendar destinatario
        """)
x = input()
if int(x) == 2:
    # open file and read LINE 2
    # get values from such line
    # ask for input
    # if input is in line 2: accept operation and ask how much to transfer
    # if input is not in line 2: error - ask would you like to add them?
    # ask for CBU or alias
    a = 0
    c = []
    while a == 0:
        b = input("ingrese huevada: ")
        secLine = open(y,"r")
        valSecLine = secLine.readlines()[1]
        secLine.close()
        print(valSecLine)
        

        if b == "exit":
            print(c)
            a = 1
        else:
            c.append(b)

