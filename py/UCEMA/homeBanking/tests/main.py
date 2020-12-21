import os
import pickle
from pathlib import Path


y = input('who the fuck are you? ')
b = input("ingresá algo: ")
data = [0, []]
check = os.path.isfile(y)
if check == False:

    file = open(y, "x")
    file.close()
    file_size = Path(f"{y}").stat().st_size
    if file_size == 0:
        # creates a binary file and adds information on line 8
        file = open(y, "wb")
        pickle.dump(data,file)
        file.close()
        
        # open file and get elements on the second elemento of the list
        f = open(y,"rb")
        read = pickle.load(f)
        print(read[1])
        f.close()

        # open file and write to element 2, which is another list
        t = open(y, "wb")
        read[1].append(b)
        t.close()

        p = open(y,"rb")
        e = pickle.load(p)
        print(e)
        f.close()
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

