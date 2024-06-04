# La sentencia if
temperature = 40

if temperature > 35:
    print("Aviso por alta temperatura")

# La sentencia if-else
temperature = 20

if temperature > 35:
    print("Aviso por alta temperatura")
else:
    print("Parámetros normales!")

# La sentencia if anidada
temperature = 28

if temperature < 20:
    if temperature < 10:
        print("Nivel azul")
    else:
        print("Nivel verde")
else:
    if temperature < 30:
        print("Nivel naranja")
    else:
        print("Nivel rojo")

# La sentencia anidada con elif
temperature = 40

if temperature < 20:
    if temperature < 10:
        print("Nivel azul")
    else:
        print("Nivel verde")
elif temperature < 30:
    print("Nivel naranja")
else:
    print("Nivel rojo")

# Asignación condicional de una única línea
fireRisk = "LOW" if temperature < 30 else "HIGHT"
print(fireRisk)

# SENTENCIA MATCH-CASE
color = "verde"

match color:
    case "rojo":
        print("Color rojo")
    case "amarillo":
        print("Color amarillo")
    case "verde":
        print("Color verde")
    case "azul":
        print("Color azul")
    case _:
        print("Color desconocido!")
