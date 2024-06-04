# Las tuplas admiten diferentes tipos de datos -> ("a", 1, True)
emptyTuple = ()
tenerifeGeoloc = (26.345, -16.789)
threeMen = ("melchor", "gaspar", "baltasar")

# Tuplas de un elemento -> Añadir una coma al final
oneItemTuple = ("papá noel",)
print(oneItemTuple)
print(type(oneItemTuple))

# Tuplas sin paréntesis
example = "melchor", "gaspar", "baltasar"
print(type(example))

# Modificar una tupla -> Son inmutables, es decir, no puede ser modificada ❌

# Conversión -> tuple() -> strings, listas, diccionarios, conjuntos, etc ✅.
# number ❌
# tuple() sin argumentos equivale a una tupla vacía.
shopping = ["agua", "aceite", "huevo"]
print(tuple(shopping))

"""
OPERACIONES CON TUPLAS:
reverse, append, extend, remove, clear, sort.
"""

# Desempaquetado de tuplas -> Asignar tuplas a variables independientes.
threeWiseMen = ("Melchor", "gaspar", "baltasar")
king1, king2, king3 = threeWiseMen
print(king1, king2, king3)

# Python ofrece la función divmod() que devuelve el cociente y el resto de una
# División usando una única llamada.
quiotient, remainder = divmod(7, 3)
print(quiotient)
print(remainder)

#  Intercambio de valores -> Desde el desempaquetado.
value1 = 40
value2 = 20
value1, value2 = value2, value1
print(value1)
print(value2)

# Desempaquetado extendido -> Operador *
ranking = ("G", "A", "R", "Y", "W")
head, *body, tail = ranking
print(head)
print(body)
print(tail)

# Desempaquetado genérico
# Sobre cadenas de texto
oxygen = "02"
first, last = oxygen
print(first, last)

text = "Hello, world"
head, *body, tail = text
print(head, body, tail)

# Sobre listas
writer1, writer2, writer3 = ["virginia woolf", "jane austen", "mary shelley"]
print(writer1, writer2, writer3)

text = "Hello, World!"
word1, word2 = text.split()
print(word1, word2)
