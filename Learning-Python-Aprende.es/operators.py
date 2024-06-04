"""
?  OPERADORES DE COMPARACIÓN:
Igualdad -> ==
Diferente -> !=
Menor que -> <
Mayor que -> >
Menor o igual que -> <=
Mayor o igual que -> >=
"""

value = 8
print(value == 8)
print(value != 8)
print(value < 12)
print(value <= 7)
print(value > 4)
print(value >= 9)

"""
? OPERADORES LÓGICOS:
and, or, not
! Tabla de la verdad por cada operador lógico:
True and True
False and True
True and False
False and False

True or True
False or True
True or False
False or False
"""

# Cortocircuito -> Cuando la evaluación de una expresión se detiene debido a que
# Ya conoce el valor final.
power = 10
signal_4g = 60
print(power > 25 and signal_4g > 10)

powerTwo = 50
signalTwo_4g = 20
print(powerTwo > 40 or signalTwo_4g > 30)

# BOOLEANOS EN CONDICIONES:
is_cold = True
if is_cold:
    print("Coge chaqueta!")
else:
    print("Usa camiseta!")

if not is_cold:
    print("Usa saco!")
else:
    print("Usa un buso!")

# VALOR NULO -> None es un valor especial que almacena el valor nulo
valorNulo = None
if valorNulo:
    print("Value has some useful value")
else:
    print("Value seems to be void")

# Preguntar si algo no es nulo:
value = 99
if value is not None:
    print(f"{value}")

# VALORES QUE SON FALSY
bool(False)
bool(None)
bool(0)
bool(0.0)
bool("")
bool([])
bool(())
bool({})
bool(set())

# VALORES QUE SON TRUTHY
bool("false")
bool(" ")
bool("1e-10")
bool([0])
bool("🐱‍👤")

# ASIGNACIÓN LÓGICA -> OR Y AND
b = 0
c = 5
# 0 se evalúa como False
a = b or c
print(a)

b = 0
c = 6
# 0 evalúa False al utilizar and
a = b and c
print(a)

# OPERADOR MORSA: := Permite realizar asignaciones dentro de expresiones.
radio = 4.25
if (perimetro := 2 * 3.14 * radio) < 100:
    print("Increase radius to reach minimum perimeter")
    print("Actual perimeter: ", perimetro)
