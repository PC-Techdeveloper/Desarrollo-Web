# Las tuplas son tipos de datos que no se pueden modificar (inmutables)
# Métodos -> tuple, count, index y join

# Tupla vacía
empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))

# Tuple with initial values
frutas = ("banano", "naranja", "mango", "limon")

# Len -> Longitud
print(len(frutas))

# Acceder desde los índices (Posición)
print(frutas[0])
print(frutas[-3])

# Slicing tuples -> Doesn't include item [1:3] -> ❌
# Range of positive and negative indexes -> All items -> ✅
print(frutas[0:4])
print(frutas[-4:])

# Changing tuples to list or list to tuples
fruta_en_lista = list(frutas)
print(fruta_en_lista)
fruta_en_tupla = tuple(frutas)
print(fruta_en_tupla)

# Checking item in a tuple -> in -> Boolean (True/False)
print("mango" in frutas)
print("sandia" in frutas)

# Joining tuples -> + operator
marcas_de_carros = ("chevrolet", "mercedez", "bmw")
marcas_de_motos = ("yamaha", "honda", "suzuki")
print(marcas_de_carros + marcas_de_motos)

# Deleting tuples -> del
marcas_de_motos = ("yamaha", "honda", "suzuki")
del marcas_de_motos
