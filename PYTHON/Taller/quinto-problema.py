print("*** INGRESANDO NÚMEROS MENORES O IGUALES A 25***")

print()


def numerosMenoresOIguales():
    # Los números se irán agregando con una lista vacía
    numeros = []
    # Utilizando el método range para iterar números con un bucle for
    for i in range(20):
        # Ingresando los datos
        numero = int(input(f"Ingrese el número {i + 1}: "))
        # Agregando los números a la lista
        numeros.append(numero)

    print()

    print("Los números menores o iguales a 25 son:")
    # Iterar los números menores o iguales a 25
    for numero in numeros:
        if numero <= 25:
            print(numero)


numerosMenoresOIguales()
