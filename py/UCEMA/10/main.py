"""Escribir un programa que imprima todos múltiplos de un número ‘n’ entero entre 1 y 9 que ingresa el usuario hasta el 30. Si el número se encuentra fuera del rango anterior imprimir el mensaje “El número debe ser un valor entero entre 1 y 9”."""

numero = int(input('ingrese un n√∫mero: '))

if numero < 1 or numero > 9:
  print('El n√∫mero debe ser un valor entero entre 1 y 9')
else:
  for x in range(1,31):
    multiplo = (numero*x)
    if multiplo <= 30:
      print(multiplo)
