"""
Los diccionarios son una coleccioón de tipos de datos emparejados (clave:valor), modificables (mutables) y desordenados.
"""

# Empty dict
empty_dict = {}

# Dictionary with data values -> list, tuple, boolean, string
person = {
    "first_name": "Asabeneh",
    "last_name": "yetayeh",
    "age": 250,
    "country": "findland",
    "is_married": True,
    "skillS": ["javascript", "react", "node", "mongoDb", "python"],
    "address": {"street": "space street", "zipcode": "02210"},
}

# Dictionary lengths
print(len(person))

# Accesing dictionary items
print(person["first_name"])
print(person["skillS"])

# Accesing by key -> Method get()
print(person.get("country"))

# Adding items to a dictionary
# append -> Agrega un elemento al principio del diccionario
person["job_title"] = "Instructor"
person["skillS"].append("html")
print(person)

# Modifying items in a dictionary
person["first_name"] = "Eyob"
person["age"] = 252
print(person)

# Checking keys in a dictionary -> Boolean -> True/False
print("job_title" in person)
print("key" in person)

# Removing key and value pairs from a dictionary
"""
pop(key)
pop(item)
del
"""
person.pop("first_name")
# Elimina el elemento de address
person.popitem()
del person["is_married"]
print(person)

# Changing dictionary to a list of items
# items -> Cambia el diccionario a una "lista" de "tuplas"
print(person.items())

# Clearing a dictionary
person2 = {"first_name": "Jefferson", "last_name": "Chavez Diaz", "age": 24}
# del person2

# Copy a dictionary
# copy -> Copia identica
copia_person2 = person2.copy()
print(copia_person2)

# Getting dictionary keys as a list
numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print(numbers.keys())

# Getting dictionary values as a list
print(numbers.values())
