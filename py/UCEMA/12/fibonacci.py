numero = int(input('ingresa un numero: '))

def Fibonacci(n=1, a=0, b=1):
  print(a)
  for i in range(n-1):
    c = a + b
    print(c)
    b = a 
    a = c

Fibonacci(numero)
