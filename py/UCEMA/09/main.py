"""Escribir programa que reciba un numero y realice una cuenta regresiva por consola hasta 0 haciendo uso de la estructura while. Si el numero ingresado es 0 o negativo mostrar por consola El numero debe ser positivo."""

numero = int(input('ingrese un numero: '))

asdf = 0

while asdf == 0:
  if numero <= 0:
    numero = int(input('El numero debe ser positivo: '))
  elif numero > 0:
    numero -= 1
    print(numero)
    if numero == 0:
      asdf = 1
