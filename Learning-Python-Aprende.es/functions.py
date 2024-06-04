# Definiendo una función
def say_hello():
    print("Hello")


# Invocando una función
say_hello()


# Retornando un valor
def one():
    return 1


print(one())
# Asignar la función a una variable y utilizarla:
value = one()
print(value)

# Integrar en expresiones como en las condicionales:
if one() == 1:
    print("It works!")
else:
    print("Something is broken")


# Si una función no incluye 'return', devolverá 'None'
def empty():
    x = 0
    return None


print(empty())


# Return a secas que devolverá 'None' y hace que salgamos de la función:
def quick():
    return


print(quick())


# RETORNANDO MÚLTIPLES VALORES -> El secreto está en hacerlo mediante una tupla.
def multiple():
    return 0, 1  # Es una tupla?


print(multiple())
print(type(multiple()))

# Por lo tanto, podemos aplicar el desempaquetado de tuplas sobre el valor retornado
# Por la función
a, b = multiple()
print(a)
print(b)

"""
PARÁMETROS Y ARGUMENTOS:
"""


# Función que recibe un parámetro
def sqrt(value):
    return value ** (1 / 2)


resultado = sqrt(4)
print(resultado)


def _min(a, b):
    if a < b:
        return a
    return b


# Función que recibe un argumento
print(_min(4, 3))

"""
ARGUMENTOS POSICIONALES: Son aquellos argumentos que se copian en sus correspondientes parámetros por orden de escritura.
"""


# Función que construye un CPU a partir de 3 parámetros:
def build_cpu(vendor, num_cores, freq):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


# Invocando a una función con argumentos posicionales:
print(build_cpu("AMD", 8, 2.7))

"""
ARGUMENTOS NOMINALES: Los argumentos se asignan por nombre a cada parámetro. Ello nos permite evitar el problema de conocer cuál es el orden de los parámetros en la definición de la función.
"""
# Invocando a la función build_cpu con argumentos nominales:
# El orden de los argumentos no influyen en el resultado final:
print(build_cpu(num_cores=8, freq=2.7, vendor="AMD"))

"""
ARGUMENTOS POSICIONALES Y NOMINALES: Python permite mezclar argumentos posicionales y nominales en la llamada a una función.
"""
# Los argumentos posicionales siempre deben ir ANTES que los argumentos nominales:
resultado_pc = build_cpu("INTEL", num_cores=4, freq=3.1)
print(resultado_pc)

"""
PARÁMETROS POR DEFECTO: Es posible específicar valores por defecto en los parámetros de una función. En el caso de que no se proporcione un valor al argumento en la llamada a la función, el parámetro correspondiente tomará el valor definido por defecto.
"""


def build_second_cpu(vendor, num_cores, freq=3.5):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


# Llamada a la función sin específicar frecuencia de CPU:
print(build_second_cpu("INTEL", 2))
# Llamada a la función indicando una frecuencia concreta de CPU:
print(build_second_cpu("RYZEN", 5, 3.4))

"""
MODIFICANDO PARÁMETROS MUTABLES:
"""


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy("a, b, c", [])


# Ccódigo anterior con un tipo de dato inmutable teniendo en cuenta la primera llamada.
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nonbuggy("a")
nonbuggy("b")
nonbuggy("a", ["x", "y", "z"])
nonbuggy("b", ["x", "y", "z"])

"""
EMPAQUETAR/DESEMPAQUETAR ARGUMENTOS:
"""


# Empaquetar argumentos posicionales -> Operador * en una tupla

values = (4, 3, 2, 1)


def _sum(*values):
    print(f"{values}")
    result = 0
    for value in values:
        result += value
    return result


# print(_sum(4, 3, 2, 1))
# Desempaquetado de values
_sum(*values)


# EMPAQUETAR/DESEMPAQUETAR ARGUMENTOS NOMINALES -> Operador ** en un diccionario:

marks = dict(ana=8, antonio=6, inma=9, javier=7)


def best_student(**marks):
    print(f"{marks= }")
    max_mark = -1

    for student, mark in marks.items():
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student


# print(best_student(Ana=8, Antonio=6, Inma=9, Javier=7))
# Desempaquetado de marks
print(best_student(**marks))


# Convenciones -> args(argumentos posicionales), kwargs(argumentos nominales)
def func(*args, **kwargs):
    # TODO
    pass


# FORZANDO MODO DE PASO DE ARGUMENTOS
# ARGUMENTOS SÓLO NOMINALES:
"""
En la definición de los parámetros de la función, se incluye el parámetro especial *, que delimitará el tipo de parámetros. Así, todos los parámetros de la derecha del separador estarán obligados a ser nominales. SEPARADOR = *
"""


def sum_power(a, b, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(sum_power(3, 4))
print(sum_power(a=3, b=4))
print(sum_power(3, 4, power=True))

# ARGUMENTOS SOLO POSICIONALES:
"""
En la definición de los parámetros de la función, tendremos que incluir un parámetro especial / que delimitará el tipo de parámetros. Así, todos los parámetros a la izquierda del delimitador estarán obligados a ser posicionales. SEPARADOR = /
"""


def sumPower(a, b, /, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(sumPower(4, 4))
print(sumPower(4, 4, True))
print(sumPower(4, 4, power=True))


# FIJANDO ARGUMENTOS POSICIONALES Y NOMINALES -> COMBINACIÓN:
def sum_power(a, b, /, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


sum_power(3, 4, power=True)

"""
function_argsES COMO PARÁMETROS:
"""


# Pasando una función como parámetro:
def success():
    print("Yeah!")


def doit(f):
    f()


doit(success)


# Pasando una función como argumentos con valores a operar -> 🟨
def repeat_please(text, times=1):
    return text * times


def doit(f, arg1, arg2):
    return f(arg1, arg2)


function_args = doit(repeat_please, "Functions as params ", 3)
print(function_args)


# DOCUMENTACIÓN -> Adjuntar documentación a la definición de una función incluyendo
# una cadena de texto (docstring) al comienzo de su cuerpo:
def sqrt(value):
    "Returns the square root of the value"
    return value ** (1 / 2)


def closet_int(value):
    """
    Returns the closet integer to the given value.
    The operations is:
        1. Compute distance to floor.
        2. If distance less than a half, return floor otherwise, return ceil.
    """
    floor = int(value)
    if value == floor * 0.5:
        return floor
    else:
        return floor + 1


# Para ver la documentación docstring de una función, basta con utilizar help() o ?
# help(closet_int)

"""
ANOTACIÓN DE TIPOS EN LAS FUNCIONES -> Las anotaciones de tipo o type-hints permiten indicar tipos para los parámetros de una función y/o para su valor de retorno (aunque también funcionan en la creación de variables).
"""


# Con los tipos (:), con el valor de retorno (->)
def ssplit(text: str, split_pos: int) -> tuple:
    return text[split_pos], text[split_pos]


print(ssplit("Always remeber us this way", 15))
print(ssplit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))


# VALORES POR DEFECTO para los parámetros:
def ssplit(text: str, split_pos: int = -1) -> tuple:
    if split_pos == -1:
        split_pos = len(text) // 2
    return text[:split_pos], text[split_pos:]


print(ssplit("Always remember us this way!"))

"""
TIPOS COMPUESTOS: Indicar una lista de cadenas de texto o un conjunto de enteros.

list[str] -> ["A","B","C"]
set[int] -> {4,3,9}
dict[str, float] -> {"a": 3.786, "y": 2.198, "x": 4.354}
tuple[str, int] -> ("Hello, 10)
tuple[float, ...] -> (1, 23, 5.21) o (4.31, 6.87) o (7.11)

MÚLTIPLES TIPOS: Determinar un parámetro que puede ser de un tipo o de otro con el operador |.

tuple|diccionario -> Tupla o diccionario
list[str|int] -> Lista de cadenas de texto y/o enteros
set[int|float] -> Conjunto de enteros y/o flotantes.
"""


# Número indefinido -> Cuando se trabaja con parámetros que representan un número
# indefinido de valores, no es necesario indicar que es una tupla.
def _max(*args: int | float):
    pass


"""
TIPOS DE FUNCIONES:
"""


# Función lambda -> Se escribe en una única línea, no tiene nombre, contiene un return y puede recibir cualquier número de parámetros.


def num_words(text: str) -> int:
    return len(text.split())


# Transformación en función lambda:
numWords = lambda texto: len(texto.split())
print(numWords("Hola"))
print(type(numWords))

# Tabla de operador lógico and (&)
logic_and = lambda x, y: x & y
for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {logic_and(i , j)}")

"""
LAMBDAS COMO ARGUMENTOS: Las funciones lambda son bastante utilizados como argumentos a otras funciones.
"""
geoloc = (
    (15.623037, 13.258358),
    (55.147488, -2.667338),
    (54.572062, -73.285171),
    (3.152857, 115.327724),
    (-40.454262, 172.318877),
)

# Ordenación por longitud (primer elemento de la tupla)
print(sorted(geoloc))

# Ordenación por longitud (segundo elemento de la tupla)
print(sorted(geoloc, key=lambda texto: texto[1]))


"""
FUNCIONES RECURSIVAS: La recursividad es el mecanismo por el cual una función se llama a sí misma.
"""


def call_me():
    return call_me()


def pow(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    return base * pow(base, exponente - 1)


print(pow(2, 4))
print(pow(3, 5))


# Calcular la suma de las longitudes de una serie de palabras:
def get_size(words: list[str]) -> int:
    if len(words) == 0:
        return 0
    return len(words[0]) + get_size(words[1:])


words = ["This", "is", "recursive"]
print(get_size(words))

"""
DECORADORES: Un decorador es una función que recibe como parámetro una función y devuelve otra función, se podría ver como una clausura:
"""
"""
my_decorator -> Nombre del decorador
wrapper -> Función interior
func -> Función a decorar
*args -> Argumentos posicionales
**kwargs -> Argumentos nominales
"""


# Decorador que convierte el resultado númerico en una función
# a su representación binaria


def res2bin(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return bin(resultado)

    return wrapper


# Definiendo una función ordinaria


def power(x: int, n: int) -> int:
    return x**n


print(power(4, 5))

# Aplicando el decorador definido previamente
# res2bin() es la función decoradora y power() es la función decorada.

decorated_power = res2bin(power)
print(decorated_power(2, 3))
print(decorated_power(4, 5))

"""
CLAUSURAS: Una clausura establece el uso de una función interior que se genera dinámicamente y recuerda los valores de los argumentos con los que fue creada.
"""


# Clausura que permite generar una tabla de múltiplicar:
def makeMultiplierOf(n: int):
    def multiplier(x: int) -> int:
        return x * n

    return multiplier  # Factoria de funciones


# Retornando una función
m3 = makeMultiplierOf(5)(8)
print(m3)
