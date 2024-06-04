"""
Assert: Esta sentencia nos permite comprobar si se están cumpliendo las «expectativas» de nuestro programa, y en caso contrario, lanza una excepción informativa.
"""

# result = 10

# assert result > 0

# print(result)

"""
Si la condición no se cumple, la aserción devuelve un error 'AssertionError' y el programa interrumpe su ejecución.
"""

result = -1

assert result > 0, "El resultado debe ser positivo!"
print(result)
