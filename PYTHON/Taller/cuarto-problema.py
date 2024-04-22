print("*** AÑOS PARA DOBLAR ***")

print()


def años_para_doblar(capital, tasaDeInteres):
    # Iniciar el año en 0
    años = 0
    capitalActual = capital

    while capitalActual < capital * 2:
        # Calculando el nuevo valor del capital después de un año
        capitalActual *= 1 + tasaDeInteres
        # Incrementando en uno ya que ha pasado 1 año
        años += 1

    return años


capital = float(input("Ingrese el capital inicial: "))
tasaDeInteres = float(input("Ingrese la tasa de interés anual (en decimal): "))

años = años_para_doblar(capital, tasaDeInteres)
print(f"El capital se doblará después de {años} años.")
