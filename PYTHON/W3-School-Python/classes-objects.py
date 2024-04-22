"""
Python is an object oriented programming language, almost everything in Python is an object, with its properties and methods. A class is like an object constructor, or a 'blueprint' for creating objects.
"""

# Create a class


class MyClass:
    x = 5


# Create object

p1 = MyClass()

print(p1.x)


"""
THE __INIT__() FUNCTION:

All classes have a function called __init__(), which is always executed when the class is begin initiated. Use the __init__() function to assign values to objecct properties or, other operations that are necessary to do when the object is begin created:
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("John", 36)

print(person1.name)
print(person1.age)


"""
THE __STR__() FUNCTION: The __str__() function controls what should be returned when the class object is a represented as a string. If __str__() function is not set, the string representation of the object is returned:
"""


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


person_1 = Person2("Jhonatan", 24)

print(person_1)


"""
OBJECT METHODS: Objects can also contain methods. Methods in objects are functions that belong to the object.
"""


class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person3("Maria", 26)

p1.myfunc()


"""
THE SELF PARAMETER: The 'self' parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class:
"""


class Person4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods:
    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person4("John", 36)
# MODIFY PROPERTIES ON OBJECTS:
p1.age = 40

print(p1.age)

"""
PYTHON INHERITANCE:

1. Parent class: Is the class being inherieted from, also called base class.
2. Child class is that inherits from another class, also called derived class.
"""


# Parent class:
class Person5:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(self.firstName, self.lastName)


primerPersona = Person5("James", "Rodriguez")

primerPersona.printName()

# Child class:


# Add the __init__ function to the Student class:
class Student(Person5):
    def __init__(self, firstName, lastName, year):
        super().__init__(firstName, lastName)
        self.graduationyear = year

    # Add a method
    def welcome(self):
        print(
            f"Welcome {self.firstName, self.lastName} to the class of {self.graduationyear}"
        )


estudiante = Student("Mike", "Olsen", 2019)

estudiante.welcome()
