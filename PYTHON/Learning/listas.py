"""
1. Listas -> Es una colección de datos ordenadas y modificable, permite miembros duplicados.
2. Tuplas -> Es una colección de datos ordenadas e inmutables o inmodificables, permite miembros duplicados.
3. Conjuntos -> Es una colección de datos desordenada, no inexada y no modificable. Pero permite agregar nuevos elementos al conjunto,no se permiten duplicados.
4. Diccionarios -> Es una colección de datos desordenada, modificable e indexada. No hay miembros duplicados.
"""

# Lista vacía
lista = list()

# Lista con valores iniciales
frutas = ["banana", "naranja", "mango", "limon"]
vegetagles = ["tomate", "papa", "repollo", "cebolla", "zanahoria"]

# Las listas pueden contener diferentes tipos de datos
lista2 = ["Asabeneh", 250, True, {"country": "finland"}, (1, 2, 3)]

# Acceder a las listas por su índice, positivo y negativo
print(frutas[0])
print(frutas[-1])

# Desembalaje de elementos de la lista
elementos = ["item1", "item2", "item3", "item4", "item5"]
primer_elemento, segundo_elemento, tercer_elemento, *rest = elementos
print(primer_elemento)
print(segundo_elemento)
print(tercer_elemento)
print(rest)

# Trozos de strings -> Valores negativos y positivos
print(frutas[0:3])
print(frutas[-3:-1])

"""
MODIFICAR ELEMENTOS DE UNA LISTA:
"""
# Primer elemento banana por avocado
frutas[0] = "avocado"
print(frutas)
# Ultimo elemento limon por sandia
frutas[-1] = "sandia"
print(frutas)

"""
AGREGAR ELEMENTOS A UNA LISTA -> MÉTODO
append -> Agrega un elemento al final.
"""
frutas.append("manzana")
print(frutas)

"""
INSERTAR ELEMENTOS ENTRE UNA LISTA -> MÉTODO
insert -> Agrega elemento por posición de índice y añadir el elemento.
"""
frutas.insert(1, "uva")
print(frutas)

"""
ELIMINANDO ELEMENTOS DE UNA LISTA -> MÉTODOS
remove -> Elimina un elemento específico de una lista.
pop -> Elimina el último elemento de una lista o desde su posición.
del -> Elimina una lista desde su posición.
clear -> Elimina toda la lista
"""
frutas.remove("manzana")
print(frutas)
frutas.pop()
print(frutas)
frutas.pop(2)
print(frutas)

# Eliminando lista por posición con del
frutas = ["banana", "naranja", "mango", "limon"]
del frutas[3]
print(frutas)
# Eliminando trozos de elementos de una lista
del frutas[1:3]
print(frutas)
# Eliminando toda la lista por completo
frutas.clear()
print(frutas)

"""
COPIAR UNA LISTA -> MÉTODO
copy -> Copia una misma lista que la original
"""
vegetagles = ["tomate", "papa", "repollo", "cebolla", "zanahoria"]
copia_vegetables = vegetagles.copy()
print(copia_vegetables)

"""
UNIÓN DE LISTAS -> MÉTODOS
Operador + -> Concatena .
extend -> Agrega una lista junto con otra lista.
"""
# Con método extend
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]
numeros1.extend(numeros2)
print(numeros1)
# Con operador +
numeros3 = [1, 2, 3]
numeros4 = [4, 5, 6]
print(numeros3 + numeros4)

"""
CONTAR ELEMENTOS DE UNA LISTA -> MÉTODO
count -> Devuelve el número de veces que aparece un elemento en una lista.
"""
edades = [22, 19, 24, 25, 26, 24, 25, 24]
print(edades.count(24))

"""
ENCONTRAR EL ÍNDICE DE UN ELEMENTO DE UNA LISTA -> MÉTODO
index -> Devuelve el índice de un elemento.
"""
edades2 = [23, 45, 76, 12, 56]
print(edades2.index(76))

"""
INVERTIR UNA LISTA -> MÉTODO
reverse -> Invierte el orden de los elementos de una lista.
"""
fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)

"""
CLASIFICAR UNA LISTA DE MANERA ASCENDENTE Y DESCENDENTE -> MÉTODOS
sort -> Ordena elementos de manera ascendente.
sorted -> Ordena elementos de manera descendente.
"""
# Usando sort -> Ascendente de manera alfabética
fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()
print(fruits)
# Usando sorted -> Descendente
fruits = ["banana", "orange", "mango", "lemon"]
print(sorted(fruits))
