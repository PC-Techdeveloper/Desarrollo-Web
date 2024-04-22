"""
Algoritmo que permita determinar si un año indicado es o no un año bisiesto.
"""

año = int(input("Por favor digite el año a evalúar: "))

if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print(f"El año {año} es bisiesto")
    año = año + 1
else:
    print(f"El año {año} no es bisiesto")
