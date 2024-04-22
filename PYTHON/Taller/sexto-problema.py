print("*** SUMANDO CAMISAS EN DÓLARES")

print()


def totalDeVentaEnPesos(precioEnDolar):
    # Cambiar Pesos a dólares
    tipoDeCambio = 20
    # Método sum para sumar elementos
    totalDeDolares = sum(precioEnDolar)
    totalEnPesos = totalDeDolares * tipoDeCambio
    return totalEnPesos


# Solicitando los precios desde una lista vacía con un bucle for ya que son números decimales
precioEnDolar = []
# 5 camisas
for i in range(5):
    precio = float(input(f"Ingrese el precio de la camisa {i+1} en dólares: "))
    precioEnDolar.append(precio)

# Calculando el total de venta en pesos
totalEnPesos = totalDeVentaEnPesos(precioEnDolar)

# Mostrando el resultado
print("El total de la venta en pesos es:", totalEnPesos)
