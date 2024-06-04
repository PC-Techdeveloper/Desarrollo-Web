# Conjunto vacío:
empty_set = set()
print(empty_set)

# Creando conjuntos -> Los conjuntos son desordenados
lottery = {21, 10, 34, 46, 55, 90, 94}

# Conversión de conjuntos: Función set() sobre cualquier iterable
# listas, conjuntos, diccionarios (extrae las claves).
print(set("aplatanada"))
print(set([1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9]))
print(("ADEDINA", "TIMINA", "TIMINA", "GUANINA", "ADENINA", "CITOSINA"))
print(set({"manzana": "rojo", "platano": "amarillo", "kiwi": "verde"}))

# Operaciones con conjuntos
# Obtener elementos -> No permite acceder a un elemento en concreto ❌
# No podemos modificar un elemento existente
# Permite añadir o borrar elementos de un conjunto -> ✅

# AÑADIR UN ELEMENTO -> add()
beatles = set(["Lennon", "McCartney", "Harrison", "Starr"])
beatles.add("Best")
print(beatles)

periodic_table = set()

metals = ("Fe", "Mg", "Au", "Au", "Zn")
periodic_table.add(metals)

nonMetals = ("C", "H", "O", "F", "Cl")
periodic_table.add(nonMetals)
print(periodic_table)

# BORRAR ELEMENTOS -> remove()
beatles.remove("Best")
print(beatles)

# LONGITUD DE UN ELEMENTO -> len()
print(len(beatles))
print()

# ITERAR SOBRE UN CONJUNTO -> bucle for
for beatle in beatles:
    print(beatle)

# PERTENCIA DE UN CONJUNTO -> IN y NOT IN
print("Lennon" in beatles)
print("Fari" not in beatles)

# ORDENANDO UN CONJUNTO -> Sorted()
marks = {8, 4, 5, 9, 2, 3}
print(sorted(marks))
print()

""" 
TEORÍA DE CONJUNTOS:
"""
A = {1, 2}
B = {2, 3}

# DIAGRAMAS DE VENN:

# Intersección -> Elementos que están a la vez en A y en B.
print("INTERSECCIÓN:")
print(A & B)
print(A.intersection(B))
print()

# Unión -> Elementos que están tanto en A como en B.
print("UNIÓN:")
print(A | B)
print(A.union(B))
print()

# Diferencia -> Elementos que están en A y no están en B.
print("DIFERENCIA:")
print(A - B)
print(A.difference(B))
print()


# Diferencia simétrica -> Elementos que están en A o en B pero no están en ambos conjuntos.
print("DIFERENCIA SIMÉTRICA:")
print(A ^ B)
print(A.symmetric_difference(B))
print()

"""
INCLUSIÓN: Comprobaciones de inclusión (subconjuntos y superconjuntos):
- Un conjunto B es un SUBCONJUNTO de otro conjunto A si todos los elementos de B están incluidos en A.
- Un conjunto A es un SUPERCONJUNTO de otro conjunto B si todos los elementos de B están incluidos en A.
"""

C = {2, 4, 6, 8, 10}
D = {4, 6, 8}

# Subconjunto:
print(C < D)
print(C <= D)

# Superconjunto:
print(C > D)
print(C >= D)
print()

# CONJUNTOS POR COMPRENSIÓN:
m3 = {number for number in range(0, 20) if number % 3 == 0}
print(m3)

# CONJUNTOS INMUTABLES -> frozenset() (Recibe cualquier iterable como argumento)
calificaciones = [1, 3, 2, 3, 1, 4, 2, 4, 5, 2, 5, 5, 3, 1, 4]
maximasCalificaciones = frozenset(calificaciones)
print(maximasCalificaciones)
