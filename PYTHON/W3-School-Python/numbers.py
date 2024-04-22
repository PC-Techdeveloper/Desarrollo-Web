"""
There are three numeric types in Python:
int, float, complex
"""

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

# INT -> Positive or negative, without decimals, of unlimited lenght.
x = 1
y = 3243453252423411
z = -23423421
print(type(x))
print(type(y))
print(type(z))

# FLOAT -> Positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an 'e' to indicate the power of 10.
x = 35e3
y = 12e4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# COMPLEX -> Complex numbers are written with a "j" as the imaginary part
x = 3 + 5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# TYPE CONVERSION -> Convert from one type to another with int(), float(), and complex()
x = 1
y = 2.8
z = 1j

# Convert from int to float:
a = float(x)

# Convert from float to int:
b = int(y)

# Convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# RANDOM NUMBER -> Make random numbers.

import random

print(random.randrange(1, 10))
