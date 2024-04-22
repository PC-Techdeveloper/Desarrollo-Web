"""
1. The 'try' block lets you test a block of code for errors
2. The 'except' block lets you handle the error
3. The 'else' block lets you execute code when there is no error
4. The 'finaly' block lets you execute code, regardless of the result of the try and except blocks 
"""

# Python normally stop and generate an error message -> Using the 'try' statement:

# X is not defined
x = 10
try:
    print(x)
except:
    print("An exception ocurred")

# MANY EXCEPTIONS:

# Except NameError:
try:
    print(x)
except NameError:
    print("Variable X is not defined")
except:
    print("Something else went wrong")

# Else:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally:
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# This can be useful to close objects and clean up resource:

try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# RISE AN EXCEPTION
# To throw (or rise) an exception, use the 'raise' keyword:
num = -1
if num < 0:
    raise Exception("Sorry!, No numbers below zero")

# Raise a TypeError if greeting is not an integers:
sayHi = "Hello"

if not type(sayHi) is int:
    raise TypeError("Only integers are allowed")
