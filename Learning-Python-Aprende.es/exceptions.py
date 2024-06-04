"""
Una excepción es el bloque de código que se lanza cuando se produce un ERROR en la ejecución del programa de Python
"""


# Error handling
# Capturing exceptions with the reserved words 'try' and 'except'
def intDiv(a, b):
    try:
        return a // b
    except:
        print("Please do not divide by zero...")


intDiv(5, 0)

"""
Aquel código que se encuentre dentro del bloque 'try' se ejecutará normalmente siempre y cuando no haya un error. Si se produce una excepción, está será capturada por el bloque 'except', ejecutándosé el código que contiene
"""

"""
La traza o pila de llamadas se muestra cada vez que se produce una excepción en nuestro programa y contiene todas las llamadas que han intervenido en el proceso. Dependiendo de lo anidado que esté el error, tendremos una traza más o menos grande
"""


# def intdiv(a: int, b: int) -> int:
#     return a // b


# def arithmetics():
#     return intdiv(3, 0)


# def manage():
#     return arithmetics()


# def main():
#     return manage()


# main()

"""
ESPECÍFICANDO EXCEPCIONES:

- TypeError: Por si los operadores no permiten la división.
- ZeroDivisionError: Por si el denominador es cero.
- Exception: Para cualquier otro error que se pueda producir.
"""


def intDivide(a, b):
    try:
        result = a // b
    except TypeError:
        print("Check operands. Some of them seems strange...")
    except ZeroDivisionError:
        print("Please do not divide by zero...")
    except Exception:
        print("Ups. Something went wrong...")


intDivide(3, 0)

intDivide(3, "0")

"""
EXCEPCIONES PREDEFINIDAS:

- AttributeError: Referencia de atributo inexistente.
- IndexError: Subíndice de secuencia fuera de rango.
- keyError: Clave de diccionario no encontrada.
- NotImplementedError: La operación debe ser - implementada.
- OSError: Error al usar una función del sistema operativo (E/S).|
- RecursionError: Alcanzado el máximo nivel de recursion.
- StopIteration: Fin del protocolo de iteración
- TypeError: Operación sobre un objeto de tipo inapropiado.
- ValueError: Operación sobre un objeto de tipo correcto pero valor inapropiado.
- ZeroDivisionError: Segundo argumento de división o módulo es cero.
"""


"""
AGRUPANDO EXCEPCIONES:
Si deseamos tratar distintas excepciones con el mismo comportamiento, es posible agruparlas en una única línea.
"""


def dividiendo(a, b):
    try:
        resultado = a // b
    except (TypeError, ZeroDivisionError):
        print("CHECK OPERANDS...")
    except Exception:
        print("UPS! is incorrect!")


dividiendo(3, 0)

"""
VARIANTES EN EL TRATAMIENTO: Python proporciona la clausula 'else' para saber que todo ha ido bien y que no se ha lanzado ninguna excepción. Esto es relevante a la hora de manejar errores. De igual modo, existe la clausula 'finally' que se ejecuta siempre, independientemente de si ha habido o no ha habido un error.
"""

valor = [4, 2, 7]

try:
    r = valor[1]
except IndexError:
    print("ERROR: Index not in list!")
else:
    print(f"Your wishes are command: {r}")
finally:
    print("Have a good day!")


"""
MOSTRANDO LOS ERRORES: Además de capturar las excepciones podemos mostrar sus mensajes de error asociados. Para ello se utiliza la palabra reservada 'as' junto a un nombre de variable que contendrá el objeto de la excepción
"""

try:
    print(valor[3])
except IndexError as error:
    # Capturando el error
    print(error)


try:
    print(valor[3])
except IndexError as error:
    print(f"Something went wrong: {error}")


"""
ELEVANDO EXCEPCIONES: Es habitual que el programa tenga que lanzar (elevar o levantar) una excepción (predefinida o propia). Para ello se utiliza la sentence 'raise'.
"""


def suma(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError("Operands must be integers")


# print(suma(4, 3))
# print(suma("x", "y"))


"""
EXCEPCIONES PROPIAS: Crear una clase heredando de Exception, la clase base para todas las excepciones, para crear una excepción propia basta con crear una clase vacía. No es necesario incluir código más alla de un 'pass'
"""


# class NotIntError(Exception):
#     pass


# values = (4, 7, 2.11, 9)

# for value in values:
#     if not isinstance(value, int):
#         # Sentencia 'raise' para elevar esta excepción
#         raise NotIntError(value)


"""
MENSAJES PERSONALIZADOS:
Python ofrece personalizar la excepción propia añadiendo un mensaje como valor por defecto.
"""


# class NotIntError(Exception):
#     def __init__(self, message="This module only with works with integers. Sorry!"):
#         super().__init__(message)


# raise NotIntError()


# Incorporar en el mensaje de la excepción el propio valor que está generando el error
# Con está misma configuración se puede personalizar el mensaje
class NotIntError(Exception):
    def __init__(self, value, *, message="Please, use integers!"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.value} -> {self.message}"


raise NotIntError(2.11)
