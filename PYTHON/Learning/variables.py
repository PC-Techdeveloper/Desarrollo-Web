nombre = "Jefferson"
apellido = "Chavez Diaz"
pais = "Colombia"
ciudad = "Cali"
edad = 24
es_casado = False
habilidades = ["html", "css", "javascript", "typescript", "python"]
informacion_personal = {
    "nombre": "Sara Michel",
    "apellido": "Delgado Diaz",
    "pais": "Colombia",
    "ciudad": "Cali",
}

# len -> Longitud
print(len(informacion_personal["nombre"]))

# Data types
print(type(apellido))
print(type(es_casado))
print(type(habilidades))

# Casting -> Convertir tipos de datos en otros.
# int to float
numero_entero = 10
numero_flotante = float(numero_entero)
print(numero_flotante)
# float to int
numeroFlotante = 25.5
numeroEntero = int(numeroFlotante)
print(numeroEntero)
# int to str
numeroEntero2 = 235
convertir_a_string = str(numeroEntero2)
print(convertir_a_string)
print(type(convertir_a_string))

"""
Números: Tipos de datos númericos
1. Enteros -> -3-2,3,2
2. Flotantes -> -3.14, 3.14
3. Complejos -> 1 + j, 2 - 4j
"""
