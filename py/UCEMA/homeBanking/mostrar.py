from vars import y

def mostrar():
    file = open(y, "r")
    print("Su saldo consolidado es de: ",file.read()) 
    file.close()
