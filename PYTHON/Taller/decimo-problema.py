print("TABLA DE MÚLTIPLICAR DECRECIENTE DE CUALQUIER NÚMERO ENTRE 1 Y 10")

print()


def tablaDeMultiplicarDecreciente(numeroIngresado):
    # Condicional if con operador lógico NOT (Verificando si el número ingresado no esta en el rango permitido que es 1 y 10)
    if not 1 <= numeroIngresado <= 10:
        print("El número ingresado está fuera del rango permitido entre 1 y 10.")
        # return para evitar que el código se continue ejecutando
        return

    # Multiplicación invertida:
    print(f"Tabla de multiplicar decreciente de {numeroIngresado}:")
    # Bucle for para iterar los números invertidos que comienzan en 10 y termina en -1 (último número)
    for i in range(10, 0, -1):
        print(f"{numeroIngresado} x {i} = {numeroIngresado * i}")


# Ingresando los números por teclado
numeroIngresado = int(input("Ingrese un número entre 1 y 10: "))

tablaDeMultiplicarDecreciente(numeroIngresado)
