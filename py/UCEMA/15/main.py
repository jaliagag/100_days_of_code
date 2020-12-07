"""Crear una función "Eliminar(lista, indice)" que reciba una lista y un numero entero. Esta debe verificar si el número está entre 0 y la última posición de la lista si es así, eliminar la posición de dicho índice y devolver la lista nueva, sino devolver la lista sin modificar."""

c = 0
l = []

while c != 1:
  a = input("ingrese un número (para salir ingrese 'n'): ")
  if a == "n":
    c = 1
  else:
    l.append(a)
    print(l)

# b = input(f'qué posición desea eliminar? (ingrese del 1 al {last}): ')
b = int(input('qué posición desea eliminar?: '))

def Eliminar(lista, indice):
  last = len(lista)
  x = 0
  while x == 0:
    if indice > last:
      indice = int(input(f'ese valor es mayor que la cantidad de elementos en la lista - tiene que insertar un valor entre el 1 y el {last}: '))
    else:
      lista.pop(indice-1)
      print(lista)
      y = input('desea eliminar algún otro valor? (s/n)')
      if y == "s":
        indice = int(input('qué posición desea eliminar?: ' ))
      else:
        print('bye!')
        x = 1
    
Eliminar(l,b)
