# Crear una lista vacía:
emptyList = []

# Crear una lista con valores:
languages = ["python", "ruby", "javascript"]
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]
data = ["Tenerife", {"cielo": "limpio", "temp": 24}, 3718, (23.23424, -16.23488)]
print(languages)
print(fibonacci)
print(data)

# Convertir listas -> list():
print(list("Python"))
print(list(range(10)))

"""
OPERACIONES CON LISTAS:
"""
# Obtener elementos:
shopping = ["agua", "huevos", "aceite", "sal", "limon"]
print(shopping[0])
print(shopping[-1])

# Trocear una lista -> Extraer carácteres:
print(shopping[0:3])
print(shopping[:3])
print(shopping[2:4])
print(shopping[-1:-4:-1])
print(shopping[::-1])

# Invertir una lista:
print(list(reversed(shopping)))

# Modificando una lista:
shopping.reverse()
print(shopping)

# Añadir al final de la lista:
shopping.append("uva")
print(shopping)

# Creando una lista desde un bucle for los números pares:
evenNumbers = []
for i in range(20):
    if i % 2 == 0:
        evenNumbers.append(i)

print(evenNumbers)

# Añadir en cualquier posición de una lista:
shopping.insert(1, "jamón")
print(shopping)

# Repetir elementos -> *:
shoppingTwo = ["agua", "carne", "papaya"]
# print(shoppingTwo * 3)

# Combinar listas:
# Conservando la lista original:
shoppingTwo = ["agua", "carne", "papaya"]
fruitShop = ["naranja", "manzana", "piña"]

listasUnidas = shoppingTwo + fruitShop
print(listasUnidas)

# Modificando la lista original -> extend():
shoppingTwo = ["agua", "carne", "papaya"]
fruitShop = ["naranja", "manzana", "piña"]

shoppingTwo.extend(fruitShop)
print(shoppingTwo)

# Modificar una lista:
shoppingTwo[1] = "jugo"
print(shoppingTwo)

# Modificar desde un troceado de carácteres:
shoppingTwo[1:4] = ["atun", "pasta"]
print(shoppingTwo)

# Borrar elementos -> PENDIENTE 🟨
# Por su índice:
del shoppingTwo[3]
print(shoppingTwo)

# Por su valor:
shoppingTwo.remove("piña")
print(shoppingTwo)

# Por su índice con extracción -> Si no coloco el índice elimina el último elemento.
shoppingTwo.pop(1)
print(shoppingTwo)

# Por su rango:
shopping[1:4] = []
print(shopping)

# Borrado completo de la lista -> clear()
shoppingTwo.clear()
print(shoppingTwo)

# Encontrar un elemento -> index, desde su posición
shoppingThree = ["huevos", "agua", "aceite", "atun", "pasta", "pera"]

print(shoppingThree.index("huevos"))

# Pertenencia de un elemento -> in (devuelve un valor booleano).
print("aceite" in shoppingThree)

# Número de ocurrencias -> count() (cuantas veces se repite).
productos = ["jabón", "clorox", "milo", "azucar", "sandia", "clorox"]

print(productos.count("clorox"))

# Dividir una cadena de texto por algún separador en lista
proverbio = "No hay mal que por bien no venga"
print(proverbio.split())

tools = "Martillo,Sierra,Destornillador"
print(tools.split(","))

# Particionado de cadenas de texto -> partition() (Es una tupla).
text = "3 + 4"

print(text.partition("+"))

# Unir una lista en cadenas de texto -> join()
tienda1 = ["agua", "sal", "galletas", "zanahoria", "cebolla"]
print("-".join(tienda1))

# Ordenar una lista:
miTienda = ["agua", "sal", "galleta", "zanahoria", "cebolla"]

# conservando la lista original
sorted(miTienda)
print(miTienda)

# Modificando la lista original
miTienda.sort()
print(miTienda)

# reverse -> Orden en sentido inverso
print(sorted(miTienda, reverse=True))

# Longitud de una lista -> len() (Conocer el número de elementos).
print(len(miTienda))

print()
# Iterar sobre una lista -> bucle for
for product in miTienda:
    print(product)

print()

# Iterando usando una enumeración -> enumerate() (Saber el índice dentro de la misma)
for i, product in enumerate(miTienda):
    print(i, product)
print()
print("*** Iterando múltiples listas ***")
# Iterar sobre múltiples listas -> zip() (Junta ambas listas elemento a elemento)
miTiendaDos = ["agua", "aceite", "arroz"]
detalles = ["mineral natural", "de oliva virgen", "basmati"]

for product, detalle in zip(miTiendaDos, detalles):
    print(product, detalle)

print()
# Lista explícita:
shopping = ["Agua", "Aceite", "Arroz"]
details = ["mineral natural", "de oliva virgen", "basmati"]

print(list(zip(shopping, details)))

print()
# Comparar listas:
print([1, 2, 3] < [1, 2, 4])

# Copias -> copy()
originalList = [4, 3, 7, 2, 1]
copyList = originalList.copy()

originalList[0] = 15
print(originalList)

print(copyList)

"""
Veracidad múltiple:
Python nos ofrece dos funciones «built-in» con las que podemos evaluar si se cumplen todas las condiciones all() o si se cumple alguna condición any(). Estas funciones trabajan sobre iterables, y el caso más evidente es una lista.
"""

# Versión clásica:
word = "python"
if len(word) > 4 and word.startswith("p") and word.count("y") >= 1:
    print("Cool word!")
else:
    print("No thanks!")

# Versión con veracidad múltiple -> all()
word = "python"
enough_length = len(word)
right_beginning = word.startswith("p")
min_ys = word.count("y") >= 1

is_cool_word = all([enough_length, right_beginning, min_ys])
if is_cool_word:
    print("Cool word!")
else:
    print("No thanks!")

# versión veracidad múltiple usando any().
word1 = "yeah"

enough_length1 = len(word1)
right_beginning1 = word1.startswith("p")
min_ys1 = word.count("y")

is_fine_word = any([enough_length1, right_beginning1, min_ys1])

if is_fine_word:
    print("Fine word")
else:
    print("No thanks")

print()

# LISTAS POR COMPRENSIÓN -> Conjuntos definidos por comprensión
# Convertir cadenas de texto con valores númericos
values = "32,45,67,89,11,20,40"

intValues = [int(value) for value in values.split(",")]
print(intValues)

# CONDICIONES EN COMPRENSIÓN
values1 = "45,12,67,34,44,98,66,30"
intValues1 = [int(v) for v in values1.split(",") if v.startswith("4")]

print(intValues1)
print()

# FUNCIONES MATEMÁTICAS:
# Suma de todos los valores:
data = [5, 3, 2, 4, 6, 7]
print(sum(data))

# Mínimo de todos los valores:
print(min(data))

# Máximo de todos los valores:
print(max(data))

# Listas de listas:
goalkeeper = "cata"
defenders = ["olga", "laia", "irene", "ona"]
midfielders = ["jenni", "teresa", "aitana"]
forwards = ["mariona", "salma", "alba"]

team = [goalkeeper, defenders, midfielders, forwards]
print(team)

# ACCEDER A DISINTOS ELEMENTOS
print(team[0])
print(team[1][0])
print(team[2])
print(team[3][1])

print()
# Recorriendo toda la alineación
for playing in team:
    if isinstance(playing, list):
        for player in playing:
            print(player, end=" ")
            print()
    else:
        print(playing)
