b = 0

while b == 0:
    a = input("muerto, incluí la cantidad de huevadas que quieras (para salir escriba exit): ")
    listarda = []
    if a != "exit":
        b = 0
        listarda.extend(a)
        print(listarda)
        print(len(listarda))

    else:
        b = 1
        print(listarda)
        print("bye, biocth!")





