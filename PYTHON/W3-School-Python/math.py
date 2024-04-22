"""
BUILT-IN MATH FUNCTION: The min() and max() functions can be use to find the lowest or hightest value in an iterable:
"""

numMin = min(5, 10, 25)
numMax = max(5, 10, 25)

print(numMin)
print(numMax)

# The abs() functions returna the absolute (positive) value of the specified number:

numAbsolute = abs(-7.25)
print(numAbsolute)

# The pow(x,y) functions return the value of x to the power of y (x^y)

numPower = pow(4, 3)
print(numPower)

"""
THE MATH MODULE
"""
import math

# The math.sqrt() returns the square root of a number:
numSqrt = math.sqrt(64)
print(numSqrt)

# The math.ceil() method rounds a number upwards to its nearest integer
# The math.floor() method rouns a number downwards to its nearest integer

numCeil = math.ceil(1.4)
numFloor = math.floor(1.4)
print(numCeil)
print(numFloor)

# The math.pi constant, returns the value of PI (3.14)
# https://www.w3schools.com/python/module_math.asp -> Math module reference
numPi = math.pi
print(numPi)
