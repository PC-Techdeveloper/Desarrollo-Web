"""
A function is a block of code which only runs when it is called, you can pass data, know as parameters, into a function. A function can return data as result.
"""


def myFunction():
    print("Hello from a function")


myFunction()

# ARGUMENTS: Inside the parentheses when you called of the function


def myFunctionTwo(myName):
    print(f"Hi, {myName} How are you!")


myFunctionTwo("Jefferson")

# ARBITRARY ARGUMENTS, *ARGS

# If the number of argument is unknown, add a * before the parameter name:


def myThirdFunction(*kids):
    print(f"The youngest child is {kids[2]}")


myThirdFunction("Emil", "Tobias", "Linus")


# KEYWORD ARGUMENTS


def my_function(child3, child2, child1):
    print(f"The youngest is {child3}")


my_function(child1="Sarah", child2="John", child3="Martha")


# ARBITRARY KEYWORDS ARGUMENTS, **KWARGS

# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function_two(**kid):
    print(f"His last name is {kid["lastName"]}")


my_function_two(firstName = "Tobias", lastName = "Calderon")


# DEFAULT PARAMETERS VALUE: If we call the function without arguments, it uses the default value:

def myFunction(country = "Norway"):
    print("I am from {}".format(country))


myFunction("Sweden")
myFunction("India")
myFunction()
myFunction("Brazil")

print()

# PASSING A LIST AS AN ARGUMENT: String, number, list, dictionary, set...

def myFunction(food):
    for fruit in food:
        print(fruit)

fruits = ["apple","banana","mango","pear","cherry"]

myFunction(fruits)

print()

# RETURNS VALUES:

def myFunction(number):
    return 5 * number

print(myFunction(3))
print(myFunction(10))
print(myFunction(5))


# THE PASS STATEMENT

def myfunction():
  pass

print()
# POSITIONAL - ONLY ARGUMENTS: To specify that a function can have only positional arguments, add , / after the arguments:

def myFunction(x, /):
    print(x)

myFunction(3)

print()


# KEYWORD - ONLY ARGUMENTS

# To specify that a function can have only keyword arguments, add *, before the arguments:

def myFunction(*, x):
    print(x) 

myFunction(x = 5)

print()


# COMBINE POSITIONAL-ONLY AND KEYWORD-ONLY

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
