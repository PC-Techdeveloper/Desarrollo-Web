# VARIABLES

# Creating variables.
x = 5
y = "John"

# Casting.
x = str(3)
y = int(3)
z = float(3)

# Get the type.
x = 5
y = "John"

print(type(x))
print(type(y))

# Single or double quotes.
x = "John"
x = "John"

# Case-Sensitive -> This will create two variables.
a = 4
A = "Sally"

# NAME

# Legal variables names:
myvar = "John"
my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# camelCase -> Each word, except the first, starts with a capital letter.
myVariable = "John"

# PascalCase -> Each word starts with a capital letter.
MyVariableName = "John"

# snake_case -> Each word is separated by an underscore character.
my_variable_name = "John"


# ASSIGN MULTIPLE VALUES
a, b, c = "Orange", "Banana", "Cherry"

# ONE VALUE TO MULTIPLE VARIABLES
x = y = z = "Paper"

"""
UNPACK A COLLECTION -> Python allows you to extract the values into variables.
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x, y, z)

# OUTPUT VARIABLES
"""
In the print() function, you output multiple variables, separated by a comma.
"""
x = "Python is awesome"
print(x)

x = "Python"
y = " is"
z = " Awesome"

# The operator + to output multiple variable
print(x + y + z)


# GLOBAL VARIABLES

"""
Global variables can be used by everyone, both inside of functions and outside.
"""
x = "awesome"


def myFunction():
    print(f"Python is {x}")


myFunction()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"


def myfunc():
    # Global variable
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)

# Scope global
x = "beautiful"


def myFunc():
    global x
    print("Python is", x)


myFunc()
