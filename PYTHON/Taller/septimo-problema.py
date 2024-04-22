print("REGISTRAR EL CONSUMO DE LOS CLIENTES EN UN RESTAURANTE")

print()

# Funcion que calcula el pago con un descuento del 20% si se excede de 50.000
def calcularElPago(consumo):
    descuento = 0
    if consumo > 50000:
        descuento = consumo * 0.20
    pago = consumo - descuento
    return pago

# Creando los clientes.
def consumoPorCliente():
    totalDePago = 0
    cantidadDeClientes = int(input("Ingresa la cantidad de los clientes: "))
    # Iterando desde el primer cliente hasta el último cliente.
    for i in range(1, cantidadDeClientes + 1):
        consumo = float(input(f"Digite el consumo del cliente {i}: "))
        # La función puede ser invocada desde una variable para ser utilizada.
        pagoPorCliente = calcularElPago(consumo)
        totalDePago += pagoPorCliente
        # Mostrando el pago por cada cliente.
        print(f"El cliente {i} debe pagar: {pagoPorCliente}")

    print(f"El total de todos los pagos es de: {totalDePago}")

consumoPorCliente()
