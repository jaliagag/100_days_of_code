# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.


#nombre = input("Ingrese su nombre\n")
#n = len(nombre)
# print(n)
#print('Su nombre,', nombre, ', tiene',n,'letras')

# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

estatura = input("¿Cuánto mides?")
peso = input("¿Cuánto pesa?")
asdf = float(estatura) * float(estatura)
print(asdf)
imc = float(peso) / float(estatura) * float(estatura)
print("Tu índice de masa corporal es de", imc)

