"""
USE THE LIST AS ARRAYS
"""
cars = ["Ford", "Volvo", "BMW"]

"""
WHAT IS AN ARRAY? 

An array is a special variable, which can hold more than one values at a time.
"""

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# GET THE VALUE OF THE FIRST ARRAY ITEM:

items = cars[0]

print(items)

# MODIFY THE VALUE OF THE FIRST ARRAY ITEMS:

cars[0] = "Toyota"

# THE LENGTH OF AN ARRAY

print(len(cars))

print()

# LOOPING ARRAY ELEMENTS

for item in cars:
    print(item)

# ADDING ARRAY ELEMENTS

cars.append("Honda")

print(cars)

# REMOVING ARRAY ELEMENTS

cars.pop(1)
cars.remove("Honda")
print(cars)
