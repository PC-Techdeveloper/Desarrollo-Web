print("*** CALCULANDO LA HORA EN EL SIGUIENTE SEGUNDO ***")

print()


# Separando la lógica para calcular el siguiente segundo desde una función
def calcularSiguienteSegundo(hora, minutos, segundos):
    # Sumando en 1 los segundos
    segundos += 1

    # Validando si llegan a 60 y 24 en horas, minutos y segundos
    # Con operador de asignación estricta para evitar un error.
    if segundos == 60:
        segundos = 0
        minutos += 1
    elif minutos == 60:
        minutos = 0
        hora += 1

    elif hora == 24:
        hora = 0

    return hora, minutos, segundos


# Función que valida la hora, minutos y segundos
def verificandoLosRangos(hora, minutos, segundos):
    return 0 <= hora <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59


# Solicitando los datos para la hota, minuto y siguiente
hora = int(input("Ingrese la hora (0-23): "))
minutos = int(input("Ingrese los minutos (0-59): "))
segundos = int(input("Ingrese los segundos (0-59): "))

if verificandoLosRangos(hora, minutos, segundos):
    nuevaHora = calcularSiguienteSegundo(hora, minutos, segundos)
    print(f"La hora en el siguiente segundo es: { nuevaHora }")
else:
    print("Los valores ingresados están fuera de rango.")
