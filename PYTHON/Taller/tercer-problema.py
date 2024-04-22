print("*** CALCULANDO LA NOTA PARCIAL ***")

print()


def calcularNotaParcial(nQuiz, nTaller1, nTaller2, nExamen):
    # Calculando el promedio de los talleres y el quiz -> 30%
    promedioTalleresQuiz = (nQuiz + nTaller1 + nTaller2) / 3 * 0.3

    # Calculando la nota del examen -> 70%
    notaExamen = nExamen * 0.7

    # Calculando la nota final del examen parcial
    notaParcial = promedioTalleresQuiz + notaExamen

    return notaParcial


# Solicitando los datos correspondientes del estudiante
nTaller1 = float(input("Nota del Taller 1: "))
nTaller2 = float(input("Nota del Taller 2: "))
nQuiz = float(input("Nota del quiz: "))
nExamen = float(input("Nota del examen parcial: "))

# Mostrando el resultado()
notaFinal = calcularNotaParcial(nQuiz, nTaller1, nTaller2, nExamen)

print(f"La nota final del primer parcial es: {notaFinal:.1f}")
