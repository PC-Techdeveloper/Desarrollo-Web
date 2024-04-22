"""
While -> Se usa para la ejecución repetida siempre que una expresión sea verdadera
"""

# Imprimiendo números del 0 al 4
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1
print()

# break -> Detiene el código -> del 0 al 2
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
print()

# continue -> Continúa el código -> del 0 al 4 (No imprime el 3)
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

print()
"""
For -> Se usa para iterar sobre los elementos de una secuencia (strings, lists, tuples) u otro objeto literable.
"""
words = ["cat", "window", "defenestrate"]
for word in words:
    print(word, len(words))

# Iterar sobre un diccionario con una copia

users = {"hans": "active", "eleonore": "inactive", "chino": "active"}
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

print(users)

# Nueva colección
active_user = {}
for user, status in users.items():
    if status == "active":
        active_user[user] = status

print(active_user)

# Iterar sobre los índices de una secuencia con range y len
a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])


# Bucle match
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(http_error(400))
