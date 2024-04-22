# Ejercicio con listas: Suma de números pares

"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

print("*** SUMAR NÚMEROS PARES ***")

numerosGanadores = []


for numeros in range(6):
    numerosGanadores.append(int(input("Digite un número ganador: ")))
numerosGanadores.sort()
print("Los números ganadores son {}".format(numerosGanadores))

print()


# Ejercicios con diccionarios: Mostrar información del usuario

"""
Escribir un programa que pregunte al usuario su address, age, city y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <name> tiene <age> años, vive en <city> y su número de teléfono es <teléfono>.
"""

print("*** INFORMACIÓN DEL USUARIO ***")

name = input("Cuál es tu nombre: ").capitalize()
age = int(input("Cuántos años tienes: "))
city = input("Cuál es tu ciudad: ").title()
phone = int(input("Cuál es tu número de teléfono: "))

user = {
    "name": name,
    "age": age,
    "city": city,
    "phone": phone,
}

print(
    f"{user["name"]}, tiene {user["age"]} años, vive en {user['city']} y su número de teléfono es {user["phone"]}"
)
