# Listas

na lista es, como se mencionó antes, una colección de datos que es característica por esta ordenada, poder cambiar y aceptar miembros duplicados. ¿Qué quiere decir esto? El orden se refiere a que los elementos que contiene tienen un orden determinado (no que si son números por ejemplo están de mayor a menor), es posible modificar valores y si se tratara de nombres por ejemplo es posible que contenga dos “Juan”. El hecho de que este ordenada implica que podemos acceder a sus elementos con índices numéricos que comienzan en 0 y al último elemento le corresponde el índice n-1 siendo n el número de elementos.

Crear dos listas, una con nombres de alumnos y otra con sus notas. Crear luego una función que reciba como parametro ambas listas y devuelva una lista en donde se encuentran la lista de nombres y la lista de notas como elementos."""

```py
nombres = ["Jose", "Paula", "Simba"]
notas = [9, 7, 2]

def combo (a, b):
  c = 0
  for i in a:
    print(i,":",b[c])
    c += 1

combo (nombres, notas)
```

Algunos de los métodos son los siguientes (para una lista llamada 'lista'):
 
- lista.append(dato): Agrega el elemento 'dato' al final de la lista
- lista.clear(): Elimina todos los elementos de la lista dejandola vacia
- lista.copy(): Devuelve una copia de la lista
- lista.count(dato): Devuelve la cantidad de elementos en la lista iguales a 'dato'
- lista.index(dato): Devuelve el índice del elemento igual a 'dato'
- lista.insert(ind, dato): Inserta 'dato' en la posición correspondiente al índice 'ind'
- lista.pop(ind): Elimina el elemento en el índice 'ind'

En el ejemplo de código se ve el uso de varios métodos además de la función len(lista) que devuelve un entero que corresponde al tamaño en este caso de la lista. Tambien se puede aplicar el operador '+' a dos listas de manera similar a dos strings, es decir que las concatena.

listaFinal = lista1 + lista2

Se puede iterar los elementos de una lista y no necesariamente a través de índices con un for de la siguiente manera:

for nombre in listaNombres:

`print(nombre)`

También es posible utilizar ‘in’ para preguntar si un valor se encuentra en una lista y devolverá true en caso de encontrarlo y false si no está

if “Juan” in listaNombres:

`print(“Juan está en la lista”)`
