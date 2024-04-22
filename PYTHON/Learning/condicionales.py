"""
Los condicionales permiten que un programa ejecutre código si se cumplen las condiciones. Se utilizan con operadores lógicos, operadores de comparación
"""

# if
a = 3
if a > 0:
    print("A es un número positivo ")

# if else
a = 3
if a < 0:
    print("A es un número negativo")
else:
    print("A es un número positivo")

# if elif else
a = -1
if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")

# if anidado
a = 4
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even integer")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")
