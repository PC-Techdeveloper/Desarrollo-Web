print("*** CALCULANDO EL TIEMPO MEDIO EN MINUTOS POR KILOMETROS ***")

print()


def calcularTiempoMedio(distanciaKm, horas, minutos):
    # Convirtiendo el tiempo total a minutos
    tiempoPorMinutos = horas * 60 + minutos

    # Calcular el tiempo medio en minutos por kilómetro
    tiempoMedioPorHoras = tiempoPorMinutos / distanciaKm

    return tiempoMedioPorHoras


# Calculando la distancia y el tiempo total de la maratón
distanciaTotalKm = float(
    input("Ingrese la distancia total de la maratón en kilómetros: ")
)
horas = int(input("Ingrese las horas totales de la maratón: "))
minutos = int(input("Ingrese los minutos totales de la maratón: "))

# Invocando a la función
tiempoMedioPorHoras = calcularTiempoMedio(distanciaTotalKm, horas, minutos)

# Imprimiendo el resultado
print(f"El tiempo medio por kilómetro es: {tiempoMedioPorHoras:.2f}")
