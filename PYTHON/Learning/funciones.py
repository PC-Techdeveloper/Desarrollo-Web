"""
Una función es un bloque reutilizable de código o declaraciones de programación diseñadas para realizar una determinada tarea.
"""


# Declaring a function
def function_name():
    print("Hola soy tu primera función en Python")


# Calling a function
print(function_name())


# Function without parameters
def generate_full_name():
    first_name = "Asabeneh"
    last_name = "Yetayeh"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name()


# Function returning a value -> Part 1
def add_two_numbers():
    num_one = 2
    num_two = 5
    total = num_one + num_two
    return total


print(add_two_numbers())


# Function with parameters
def greeting(name):
    message = f"{name}, Bienvenido a Python!"
    return message


print(greeting("Jefferson"))


# Passing arguments with key and value
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(num1=4, num2=2))


# Function returning a value -> Part 2
# string
def print_name(firstname):
    return firstname


print_name("Asabeneh")


# number
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(2, 3))


# boolean
def is_even(n):
    if n % 2 == 0:
        print("even")
        return True
    return False


print(is_even(10))
print(is_even(7))


# list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


print(find_even_numbers(10))


# Function with default parameters
def calculate_age(cumpleaños, año_nuevo=2024):
    edad = año_nuevo - cumpleaños
    return edad


print("Edad: ", calculate_age(1999))


# Argumento arbitrario -> No se sabe la cantidad de argumentos de una función -> *
def sum_all_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_numbers(2, 3, 5))


# Número predeterminado y arbitrario de parámetros en funciones
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


generate_groups("Team-1", "Asabeneh", "Brook", "David", "Eyob")


# Función como parámetro de otra función
def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))
