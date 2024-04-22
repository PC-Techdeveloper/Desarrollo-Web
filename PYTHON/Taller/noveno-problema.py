print("*** CALCULAR EL PRODUCTO DESDE 1***")

print()


def calculandoElProducto(numero):
    # Iniciando el producto en 1
    producto = 1
    # El método range inicia en 1 hasta el último número
    for i in range(1, numero + 1):
        # En cada iteración se multiplica el número actual ingresado por por el producto 1
        # 1 * 2 * 3...
        producto *= i

    return producto


# Ingresando un número.
numero = int(input("Ingrese un número entero positivo: "))

# Calculando el producto de 1 hasta N.
resultado = calculandoElProducto(numero)

# Mostrando el resultado.
print(f"El producto de todos los números desde 1 hasta {numero} es: {resultado}")
