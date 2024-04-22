"""
Set es una colección de elementos distintos desordenados y no indexados. En Python, el conjunto se utiliza para almacenar elementos únicos y es posible encontrar la unión, intersección, diferencia, diferencia simétrica, subconjunto, superconjunto y conjunto disjunto entre conjuntos.
"""

# Set empty
empty_set = set()

# Set with initial values
frutas = {"banano", "naranaja", "mango", "limon"}
print(frutas)

# len -> length of a set
print(len(frutas))

# Accesing items in a set -> Bucles
# Checking an item
print("mango" in frutas)
print("sandia" in frutas)

# Adding items to a set
# add -> Agrega elementos desordenados.
# update -> Agrega múltiples elementos desordenados
frutas.add("sandia")
print(frutas)
frutas2 = {"manzana", "pera"}
frutas.update(frutas2)
print(frutas)

# Removing items from a set
# pop -> Elimina elementos de manera desordenada.
# remove -> Elimina elementos específicos.
marcas_de_carros = {"chevrolet", "mercedez", "bmw", "ferrari"}
# marcas_de_carros.pop()
# print(marcas_de_carros)
marcas_de_carros.remove("ferrari")
print(marcas_de_carros)

# Clearing items in a set -> Empty set
marcas_de_carros.clear()
print(marcas_de_carros)

# Deleting a set
marcas_de_portatiles = {"lenovo", "asus", "dell", "toshiba"}
print(marcas_de_portatiles)
# del marcas_de_portatiles

# Converting list to a set
lista_de_herramientas = ["destornillador", "martillo", "caja"]
lista_a_conjunto = set(lista_de_herramientas)
print(lista_a_conjunto)

# Joining sets
# Method -> union
marcas_de_portatiles = {"lenovo", "asus", "dell", "toshiba"}
lista_de_herramientas = {"destornillador", "martillo", "caja"}
print(marcas_de_portatiles.union(lista_de_herramientas))

# Method -> update
marcas_de_portatiles = {"lenovo", "asus", "dell", "toshiba"}
lista_de_herramientas = {"destornillador", "martillo", "caja"}
marcas_de_portatiles.update(lista_de_herramientas)
print(marcas_de_portatiles)

# Finding intersection items -> Elementos que se encuentran en ambos conjuntos
python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
# Intersection
print(python.intersection(dragon))
print(python & dragon)

# Checking subset and super set -> Superconjunto de otros conjuntos -> True/False
python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(python.issuperset(dragon))
print(python.issubset(dragon))
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))

# Checking the difference between two sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))

# Finding symmetric difference between two sets -> Conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(even_numbers))

# Joining sets -> Si dos conjuntos no tienen uno o más elementos en común, los llamamos conjuntos disjuntos -> True/False
python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
print(python.isdisjoint(dragon))
