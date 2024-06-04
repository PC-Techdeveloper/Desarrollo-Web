# La sentencia WHILE -> Again and again until a condition is met
wantGreet = "S"
while wantGreet == "S":
    print("Hola que tal!")
    wantGreet = input("Quieres otro saludo? [S/N]: ")
print("Que tengas un buen dia!")

# Romper un bucle while con break or continue -> Limitar las repeticiones
max_greet = 4
num_greets = 0
want_greet = "S"

while want_greet == "S":
    print("Hola como estás!")
    num_greets += 1
    if num_greets == max_greet:
        print("Máximo número de saludos alcanzado!")
        break
    want_greet = input("Quieres otro saludo? [S/N]: ")
print("Que tengas un excelente resto de día!")

# BUCLE INFINITO
while 0 <= (mark := float(input("Introduce una nueva nota: "))) <= 10:
    print(mark)
print("Nota fuera de rango!")

"""
SENTENCIA FOR -> Cuando ya se sabe la cantidad de veces a repetir una instrucción.

Las estructuras de datos que permiten ser iteradas: strings, listas, diccionarios, ficheros, etc.
"""
word = "python"
for letter in word:
    print(letter)

print()

# Romper un bucle for con break o continue
myWord = "javascript"
for char in myWord:
    if char == "r":
        break
    print(char)

print()

# SECUENCIA DE NÚMEROS -> FUNCIÓN RANGE
# Inicia en 0 y termina en 2 -> 0, 1, 2
for i in range(0, 3):
    print(i)

print()

# Termina en 2 -> 0, 1, 2
for i in range(3):
    print(i)

print()

for i in range(1, 6, 2):
    print(i)

print()

for i in range(2, -1, -1):
    print(i)

print()

# Usar guión bajo como nombre de variable para repetir
# Una acción un número determinado de veces.
for _ in range(10):
    print("Repeat me 10 times!")
