"""Crear una función "NombreLargo(Nombres)" que reciba una tupla con nombres(strings) y devuelva el nombre más largo."""

def NombreLargo(Nombres):
  a = ""
  for i in Nombres:
    if len(i) > len(a):
      a = i
  print(a)

asdf = ("Jose", "Pau", "Simba")

NombreLargo(asdf)
