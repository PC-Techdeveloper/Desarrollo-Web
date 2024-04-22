print("CALCULANDO EL AREA DE FIGURAS GEOMETRICAS")

print("ÁREA DE UN CUADRADO")


def area_de_un_cuadrado():
    lado = int(input("Escribe el lado al cuadrado: "))
    operacion = 2 * lado
    return f"El área del cuadrado es: {operacion}"


# Llamando a la función
print(area_de_un_cuadrado())
print()

print("ÁREA DE UN TRIÁNGULO")


# Nombre de la función
def area_de_un_triangulo():
    base = int(input("Escribe la base del triangulo: "))
    altura = int(input("Escribe la altura del triángulo: "))
    operacion_triangulo = (base * altura) / 2
    return f"El área del triángulo: {operacion_triangulo}"


# Llamando a la función
print(area_de_un_triangulo())
print()

print("ÁREA DE UN RECTÁNGULO")


def area_de_un_rectangulo():
    ladoX = int(input("Escribe el primer lado: "))
    ladoY = int(input("Escribe el segundo lado: "))
    operacion_rectangulo = ladoX * ladoY
    return f"El área de un rectángulo es: {operacion_rectangulo}"


print(area_de_un_rectangulo())

print("FIN DEL PROGRAMA")
