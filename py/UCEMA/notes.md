# Tipos de estructura

## Listas

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

## Tuple o tupla

Otro tipo de estructura de datos que quizas no se utilice tanto como una lista es la tupla (o tuple en inglés). Esta es similar a una lista, está ordenada pero la gran diferencia que tiene es que una vez creada no se pueden modificar sus elementos. Por lo tanto puede ser útil si queremos mantener estos elementos y que no sean modificados por error. Sin embargo hay un “truco” para modificar sus valores, transformar la tupla en una lista, modificarlos y posteriormente si se quiere volver a tener una tupla de nuevo, transformar la lista ya modificada en tupla.

Declaro una tupla:

tupla = ("Juan", "Santiago", "Maria")

La forma de declarar uno es similar pero distinto a una lista. Para una tupla se encierran los datos entre paréntesis y para las listas entre corchetes.

## Set

Un set es otro tipo de estructura pero a diferencia de los anteriores no tiene orden y por lo tanto tampoco índices por lo que la única forma de recorrer uno es con un for (similar a como se recorre una lista por sus elementos y no por índices). Además tampoco admite duplicados ya que al referirse a su contenido por lo que es, si tuviera por ejemplo 2 veces a “Juan” no sabría a cual de ellos me refiero. Comparte gran cantidad de los métodos de una lista además de tener algunos característicos.

miSet = {1, 2, 3, 4, 5, 6}

Aparte de los métodos enseñados en el codigo es posible realizar algunas operaciones entre sets.(Para los sets A y B)

- A | B : A unión B generará un set que contiene los elementos que se encuentren en por lo menos uno de los dos
- A & B : A intersección B generará un set que contiene solo los elementos que se encuentran en ambos sets
- A - B : A - B devolverá un set que contiene los elementos de A que no se encuentran en B, es decir la diferencia.
- A ^ B : A ^ B Devolverá la diferencia entre ambos, es decir los elementos de ambos que no comparten.

```py
# Declaro un set
miSet = {1, 2, 3, 4, 5, 6}
print(miSet)

# Un set no puede tener elementos repetidos 
# ni tampoco estructuras que pueden cambiar como listas, diccionarios u otro set
miSet2 = {1, 2, 2, 6, 4, 3, 4}
print(miSet2)

# Si bien cuando le asigno los valores al set incluyo valores repetidos se puede ver cuando se lo imprime
# que estos los guarda solo 1 vez

# Puedo agregar solo 1 valor con el método add()
miSet2.add(20)
print(miSet2)

# O agregar varios valores con el método update() que recibe como argumentos tuplas, listas, sets o strings
miSet2.update([6, 7], {8, 3})
print(miSet2)

# El método discard() y remove() eliminan el elemento que enviamos como argumento 
# La diferencia está en que si el elemento no se encuentra en el set discard no hará nada
# En cambio remove hará que salte un error
miSet2.remove(3)
miSet2.discard(500)
print(miSet2)

for elemento in miSet2:
    print("Elemento: " + str(elemento))
    
# ejercicio

def Aprobados(materia1, materia2):
  print(materia1 & materia2)

mate = {"Jose", "Pau", "Marce", "Mariano"}
lengua = {"Jose", "Matias", "Brenda", "Marce"}
  
Aprobados(mate, lengua)
```

## Diccionario

Un diccionario es una estructura pero un poco distinta ya que no tiene orden pero si índices. Estos índices son mejor descriptos como una llave ya que lo que almacena un diccionario son valores con una llave o índice asociado pudiendo esta ser distinta a un número. Es similar a como en un diccionario uno busca la palabra (llave o índice) que desea y esta “contiene” su definición. Este tipo de estructura no admite duplicados para las llaves.

persona = {"nombre":"Juan", "edad" : 23, "sexo":"Masculino"}

En este caso las llaves o índices son nombre, edad y sexo, y cada una de ellas va acompañada del dato que le corresponde.

