"""
Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application.
"""


# Create a module: In a file with the file extension .py:
def greeting(myName):
    print("Hello, " + myName)


# IMPORT IN FILE MODULES-TWO.PY
# Variables in module -> DICTIONARIES
person1 = {"name": "John", "age": 16, "country": "Norway"}


# IMPORT FROM MODULE: Using the 'from' keyword:
def myFunction(myName):
    print("Hello, " + myName)


person2 = {"name": "Sarah", "age": 11, "country": "Colombia"}
