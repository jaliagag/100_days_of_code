from vars import y

def mostrar():
    file = open(y, "w+")
    print(file.read()) 
    file.close()
