# Los diccionarios son mutables y tienen claves únicas.
emptyDict = {}
rae = {
    "bifronte": "De dos frentes o dos caras",
    "anarcoide": "Que tiende al desorden",
    "montuvio": "Campesino de la costa",
}

populationCan = {
    2015: 2_315_203,
    2016: 4_345_676,
    2017: 1_234_670,
    2018: 2_205_604,
    2019: 4_677_888,
}

# Conversión -> dict()
# Diccionario a partir de una lista:
print(dict(["a1", "b2"]))

# Diccionario a partir de una tupla de cadenas de texto:
print(dict(("a3", "b3")))

# Diccionario a partir de una lista anidada:
print(dict([["a", 4], ["b", 4]]))


# Creación con dict()
person = dict(name="Guido", surname="Van Rossum", job="Python creator")
print(person)

"""
OPERACIONES CON DICCIONARIOS:
"""

# Obtener un elemento:
# Notación de corchetes
# Si accedemos a una clave que no existe, dará un error ❌
frases = {
    "bifronte": "De dos frentes o dos caras",
    "anarcoide": "Que tiende al desorden",
    "montuvio": "Campesino de la costa",
}
print(frases["bifronte"])

# Usando get() -> Si existe retorna el valor, sino retorna None
print(frases.get("montuvio"))
print(frases.get("programacion"))

# Añadir o modificar un elemento:
# Añadiendo elemento
frases["enjuiciar"] = "Someter una cuestión a examen, discusión y juicio"
print(frases)

# Modificando elemento:
frases["enjuiciar"] = "Instruir, juzgar o sentenciar una causa"
print(frases)

# Creando un diccionario vacío desde un bucle for
VOWELS = "aeiou"

enumVowels = {}

for i, vowel in enumerate(VOWELS, start=1):
    enumVowels[vowel] = i

print(enumVowels)

# Pertenencia de una clave -> Operador in
print("anarcoide" in frases)

# Longitud de un diccionario -> len()
print(len(frases))

# Obtener todos los elementos
# Obtener todas las claves de un diccionario -> keys()
print(frases.keys())

# Obtener todos los valores de un diccionario -> values()
print(frases.values())

# Obtener todos los elementos de un diccionario clave-valor -> items()
print(frases.items())
print()
# Iterar sobre un diccionario

# Iterar sobre claves:
for word in frases.keys():
    print(word)

print()

# Iterar sobre valores:
for meaning in frases.values():
    print(meaning)

print()

# Iterar sobre clave-valor:
for word, meaning in frases.items():
    print(f"{word}: {meaning}")

print()

# Borrar elementos -> del
del frases["bifronte"]
print(frases)

print()

# Por su clave -> Por extracción -> pop()
print(frases.pop("anarcoide"))

# Borrado completo del diccionario -> clear()

# Combinar diccionarios
# Si la clave no existe, se añade con su valor, si ya existe se añade con el valor del último diccionario en la mezcla.
print()

rae1 = {
    "bitfronte": "De dos frentes o dos caras",
    "enjuiciar": "Someter una cuestión a examen, discusión y juicio",
}

rae2 = {
    "anarcoide": "Que tiende el desorden",
    "montuvio": "Campesino de la costa",
    "enjuiciar": "Instruir, juzgar o sentenciar una causa",
}

# Sin modificar los diccionarios originales:
print({**rae1, **rae2})

print()

# Con el operador |
print(rae1 | rae2)

print()

# Modificando los diccionarios originales -> Función update()
rae1.update(rae2)
print(rae1)

# Copiar diccionarios:
originalRae = {
    "bitfronte": "De dos frente o dos caras",
    "anarcoide": "Que tiende el desorden",
    "montuvio": "Campesino de la costa",
}

copyRae = originalRae.copy()
originalRae["bitfronte"] = "bla bla bla"

print(originalRae)
print(copyRae)

# Diccionarios por comprensión:
words = ("sun", "space", "rocket", "earth")
words_length = {words: len(word) for word in words}
print(words_length)

secondWord = ("sun", "space", "rocket", "earth")
newWords = {secondWord: len(word) for word in secondWord}
print(newWords)


