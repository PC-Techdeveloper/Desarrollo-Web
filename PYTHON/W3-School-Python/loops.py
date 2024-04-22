"""
PYTHON LOOPS: Python has two primitive loop commands:

Loops while and for 
"""

# THE WHILE LOOP
# With the 'while' loop we can execute a set of statement as long as condition is true.

i = 1
while i < 6:
    print(i)
    i += 1
print()
# With the 'break' statement we can stop the loop even if the while conditionn is true.

i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print()

# With the 'continue' statement we can stop the current iteration, and continue with the next

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print()
# With the else statement we can run a block of code once when the condition no longer is true.

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

print()
"""
FOR LOOP: That is either a list, a tuple, a dictionary, a set, or a string.
"""

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

print()

# Looping throught a character.

for character in "banana":
    print(character)

print()
# With the 'break' statement we can stop the loop before it has looped throught all the items:

fruits = ["apple", "banana", "cherry"]
for element in fruits:
    print(element)
    if element == "banana":

        break
print()
# With the 'continue' we can stop the current iteration of the loop, and continue with the next

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


print()
# THE RANGE() FUNCTION:

# Returns a squence of numbers, string from 0 by default, and increments by 1, and ends at a specified number.

for number in range(2, 30, 3):
    print(number)

print()

# Else in for loop

for x in range(6):
    print(x)
else:
    print("Finally finished!")

print()

# NESTED LOOPS:

adj = ["red", "big", "tasty"]
fruitsTwo = ["apple", "mango", "papaya"]

for elementsOne in adj:
    for elementsTwo in fruitsTwo:
        print(elementsOne, elementsTwo)


# THE PASS STATEMENT: The pass statement to avoid getting an error

for x in [0, 1, 2]:
    pass
