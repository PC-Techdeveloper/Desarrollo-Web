"""
A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

SYNTAX:

lambda arguments : expression
"""

x = lambda a: a + 10
print(x(5))

# Multiply argument a with argument b and return the result.

x = lambda a, b: a * b

print(x(5, 5))

# Summarize argument a, b and c and return the result:

sumatoria = lambda a, b, c: a + b + c

print(sumatoria(5, 6, 2))

# The power of lambda is better shown when you use them aas an anonymus function inside another function:


def myFunction(n):
    return lambda a: a * n


# Doubler o triples -> 2 * 11 = 22 or 3 * 11 = 33
myDoubler = myFunction(3)

print(myDoubler(11))


# Or use, the same function definition to make both functions, in the same program:


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
