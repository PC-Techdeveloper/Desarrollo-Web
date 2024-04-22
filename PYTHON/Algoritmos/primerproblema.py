"""
Algoritmo que a partir de una fecha de nacimiento y una fecha actual determine la edad en años de una persona.
"""

print("Por favor, Ingrese la fecha de nacimiento")

# Salto de línea
print()

diaNacimiento = int(input("Dia de Nacimiento: "))
mesNacimiento = int(input("Mes de Nacimiento: "))
añoNacimiento = int(input("Año de Nacimiento: "))

print()
print("Ahora ingrese los datos de la fecha actual")
print()

diaActual = int(input("Dia actual: "))
mesActual = int(input("Mes actual: "))
añoActual = int(input("Año actual: "))

edad = añoActual - añoNacimiento

if mesNacimiento > mesActual:
    edad = edad - 1
elif mesNacimiento == mesActual:
    edad = edad - 1
elif diaNacimiento == diaActual:
    print("Felicidades hoy estás cumpliendo años")
else:
    print("Hoy no estás cumpliendo años.")

print(f"Tu edad actual es: {edad} años.")
