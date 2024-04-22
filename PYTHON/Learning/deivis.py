# personas = ["sara", "jose", "tony", "samuel"]

# comidas = ["pastas", "ensaladas", "pizza", "nachos"]

# comidas_personas = dict(zip(personas, comidas))
# print(comidas_personas)


# Construir diccionario a partir de listas

# claves = ["nombre", "apellido", "edad", "sueldo"]

# valores = []

# tamañoCampos = len(claves)

# for i in range(tamañoCampos):
#     valoracion = input("Ingrese el {}: ".format(claves[i]))
#     valores.append(valoracion)

# print(claves)
# print(valores)

# datosUsuarios = dict(zip(claves, valores))

# print(datosUsuarios)

# # Ejercicio 2

# sueldos_empleados = {
#     "Clara": 344.4,
#     "Pedro": 350.53,
#     "Roberto": 950.2,
#     "Mariano": 400.5,
#     "Deivys": 250.35,
# }

# datoConsultado = input("Dato a consultar: ")

# if datoConsultado in sueldos_empleados:
#     print(
#         "Empleado {} encontrado y gana ${}".format()(
#             datoConsultado, sueldos_empleados[datoConsultado]
#         )
#     )
# else:
#     print("No encontrado!")

# sueldos_empleados2 = {
#     "Clara": 344.4,
#     "Pedro": 350.53,
#     "Roberto": 950.2,
#     "Mariano": 400.5,
#     "Deivys": 250.35,
# }

# # Mostrando las claves de un diccionario
# for empleado in sueldos_empleados2:
#     print(empleado)

# # Mostrando clave y valor de un diccionario
# for empleado, sueldo in sueldos_empleados2.items():
#     print(empleado, sueldo)


# EJERCICIO 3

estudiantes = {"nombre": "daniel", "edad": "19", "ocupacion": "estudiante"}

# Accediendo a la clave nombre del diccionario
print(estudiantes["nombre"])

# Modificando el valor de edad y agregando un nuevo clave - valor
estudiantes["edad"] = 25
estudiantes["ciudad"] = "Cali"
estudiantes.update({"nombre": "luisa", "juego": "cartas"})

# Mostrando por pantalla
print(estudiantes)


# Eliminado la clave ocupación del diccionario estudiantes
del estudiantes["ocupacion"]
print(estudiantes)
