"""
Python has the following data types built-in by default, in the categories.

Text types -> str.
Numeric types -> int, float, complex.
Squence types -> list, tuple, range.
Mapping types -> dict.
Set types -> set, frozenset.
Boolean types -> bool.
Binary types -> bytes, bytearray, memoryview
None type -> NoneType
"""

# GETTING THE DATA TYPE
x = 9
print(type(x))

# SETTING THE DATA TYPE -> In python, the data is set when you assing a value to a variable.

a = "Hello world!"
b = 20
c = 20.5
d = 1j
e = ["apple", "banana", "cherry"]
f = ("apple", "banana", "cherry")
g = range(6)
h = {"name": "John", "age": 36}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

# SETTING THE SPECIFIC DATA TYPE -> You can the following constructor functions.

one = str("Hello World!")
two = int(40)
three = float(45.5)
four = complex(1j)
five = list(("apple", "banana", "cherry"))
six = tuple(("apple", "banana", "cherry"))
seven = dict(name="John", age=38)
eight = set(("apple", "banana", "cherry"))
nine = bool(5)
ten = bytes(5)

print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)
print(ten)
