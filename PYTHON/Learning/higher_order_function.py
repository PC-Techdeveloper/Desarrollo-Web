# Función como parámetro


def sum_numbers(nums):
    return sum(nums)


def higher_order_function(f, lista):
    summation = f(lista)
    return summation


print(higher_order_function(sum_numbers, [1, 2, 3, 4, 5]))

# Función como valor de retorno


def square(x):
    return x**2


def cube(x):
    return x**3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function2(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute
    else:
        return "Incorrecto!"


result = higher_order_function2("cube")
print(result(10))
