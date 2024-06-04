"""
PROGRAMACIÓN ORIENTADA A OBJETOS:
- Encapsulamiento: Permite empaquetar el código de una unidad (objeto) donde se puede determinar el ámbito de actuación.

- Abstracción: Permite generalizar los tipos de objetos a través de las clases y simplificar el programa.

- Herencia: Permite reutilizar el poder heredar atributos y comportamientos de una clase a otra.

- Polimorfismo: Permite crear múltiples objetos a partir de una misma pieza flexible de código.

¿QUÉ ES UN OBJETO?:
Un objeto representa una instancia única de alguna entidad (a través de los valores de sus atributos) e interactua con otros objetos (o consigo mismo) a través de sus métodos.

¿QUÉ ES UNA CLASE?
Para crear un objeto primero debemos definir la clase que lo contiene. La clase es como un molde con el que se crean nuevos objetos de ese tipo.
"""

# Creando objetos -> Palabra reservada 'class':
# Los nombres de la clase se escriben en formato CamelCase:


class StarWarsDroid:
    pass


# Crear instancias/objetos de droides:
droide1 = StarWarsDroid()
droide2 = StarWarsDroid()
droide3 = StarWarsDroid()

"""
Añadiendo métodos: Un método es una función que forma parte de una clase o de un objeto. En su ámbito tiene acceso a otros métodos y atributos de la clase o del objeto al que pertenece. Incorporando un primer parámetro 'self' que hace referencia a la instancia actual del objeto.
"""


class Droide:

    # Declarando un método de la clase Droide:
    def switch_on(self):
        return "Hola soy un androide encendido!"

    def switch_off(self):
        return "Hola soy un androide apagado!"


androide1 = Droide()
print(androide1.switch_on())

"""
AÑADIENDO ATRIBUTOS: Un atributo es una variable, un nombre al que se le asigna un valor que esta dentro de una clase o de un objeto.
"""


class DroidTwo:

    def encender(self):
        # Atributo
        self.encendido = True
        print("Hola soy un androide, en que te puedo ayudar?")

    def apagar(self):
        self.apagado = False
        print("Adiós, tengo que irme!")


droid1 = DroidTwo()

droid1.encender()
droid1.apagar()

# INICIALIZACIÓN

"""
Este método es __init__, permite asignar atributos y realizar operaciones con el objeto en el momento de su creación. También es conocido como el método constructor.
"""


# Guardando el nombre del droide como un atributo del objeto:
class Android:

    # Definición del constructor:
    def __init__(self, name: str):
        self.name = name


# Creación del objeto:
droid = Android("GB-55")

# Acceder al atributo name:
print(droid.name)

"""
ATRIBUTOS:
"""


# Acceso directo -> Modificar desde fuera con un acceso directo:
class Android2:
    def __init__(self, name: str):
        self.name = name


robot = Android2("C-3PO")

# Modificando desde fuera
robot.name = "waka-waka"
print(robot.name)

# Añadir atributos dinámicamente a un objeto después de su creación:
robot.manufacturer = "Cybot Galactice"
robot.height = 1.77

"""
PROPIEDADES: La forma más común de aplicar propiedades es mediante el uso de decoradores.

@property -> Para leer el valor de un atributo (getter).
@name.setter -> Para escribir el valor de un atributo.
"""


class MyDroid:
    def __init__(self, name: str):
        self.hidden_name = name

    @property
    def name(self) -> str:
        print("dentro del getter!")
        return self.hidden_name

    @name.setter
    def name(self, name) -> None:
        print("dentro del setter!")
        self.hidden_name = name


my_droid = MyDroid("N1-G3L")
my_droid.name = "waka-waka"

print(my_droid.name)
print(my_droid.hidden_name)

"""
OCULTANDO ATRIBUTOS - ENCAPSULAMIENTO: Atributos privados u ocultos con doble subguión (__)
"""


class Droide:
    def __init__(self, name: str):
        self.__name = name


droid = Droide("BC-44")

print(droid._Droide__name)

"""
Atributos de clase: Podemos asignar atributos a una clase y serán asumidos por todos los objetos instanciados de esa clase.
"""


class Droide2:
    # Obedece a su dueño
    obeys_owner = True


good_droid = Droide2()
good_droid2 = Droide2()
# El cambio no afecta a nivel de clase
print(good_droid.obeys_owner)
good_droid2.obeys_owner = False

print(good_droid2.obeys_owner)

"""
Si modificamos un atributo de clase desde un objeto, sólo modificamos el valor en el objeto y no en la clase.

Si modificamos un atributo de clase desde una clase, modificamos el valor en todos los objetos pasados y futuros.
"""


class Droides:
    obey_owner = True


droides1 = Droides()
droides2 = Droides()
droides3 = Droides()
print(droides1.obey_owner)
print(droides2.obey_owner)

# Modificando desde una clase -> Cambio pasado y futuro
Droides.obey_owner = False

print(droides1.obey_owner)
print(droides2.obey_owner)
print(droides3.obey_owner)

print(id(Droides.obey_owner))
print(id(droides1.obey_owner))
print(id(droides2.obey_owner))
print(id(droides3.obey_owner))

"""
MÉTODOS ESTÁTICOS: Es un método que no deberia modificar el estado del objeto ni de la clase. No recibe ningún parámetro especial, la identificación de estos métodos se completa aplicando el decorador '@staticmethod' a la función
"""


class Robot:
    def __init__(self):
        pass

    @staticmethod
    def get_droids_categories():
        return ("Messenger", "Astromech", "Power", "Protocol")


print(Robot.get_droids_categories())

"""
MÉTODOS MÁGICOS: Los métodos mágicos empiezan y terminan por doble subguión (__)
"""


# Para los operadores -> __eq__
class Droide:
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number

    def __eq__(self, droid: Droide):
        return self.name == droid.name


droid1 = Droide("C-3PO", 43974973242)
droid2 = Droide("C-3PO", 85094905984)

print(droid1 == droid2)
# Llamada implícita a __eq__
print(droid1.__eq__(droid2))

"""
Métodos especiales de comparación:
__eq__ -> ==
__ne__ -> !=
__lt__ -> <
__gt__ -> >
__le__ -> <=
__ge__ -> >=

Métodos especiales para operaciones matemáticas:
__add__ -> +
__sub__ -> -
__mul__ -> *
__floordiv__ -> //
__truediv__ -> /
__mod__ -> %
__pow__ -> **
"""


class Droide:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __add__(self, other: Droide) -> Droide:
        new_name = self.name + "-" + other.name
        new_power = self.power + other.power
        # Hay que devolver un objeto de tipo Droide
        return Droide(new_name, new_power)


droiden1 = Droide("C3PO", 45)
droiden2 = Droide("R2D2", 91)
droiden3 = droiden1 + droiden2

print(f"Fusión droid:\n{droiden3.name} with power {droiden3.power}")

"""
HERENCIA: La herencia consiste en construir una nueva clase partiendo de una existente, pero que añade o modifica ciertos aspectos. La herencia se considera una buena práctica de programación tanto para reutilizar código como para realizar generalizaciones.

NOMENCLATURA DE CLASES EN HERENCIA:
Clase base
superclase
clase madre
clase derivada
subclase
clase hija
"""


# Herencia desde una clase:
class Droiden:
    # *** Clase base ***
    def enciende(self):
        print("Motor encendido!")

    def apagado(self):
        print("Motor apagado!")


class ProtocolDroiden(Droiden):
    # *** Clase derivada ***
    pass


# Comprobar una herencia
print(issubclass(ProtocolDroiden, Droiden))
r2 = Droiden()
c3 = ProtocolDroiden()

r2.enciende()
r2.apagado()

# Método heredado de Droiden
c3.enciende()
c3.apagado()

"""
SOBREESCRIBIR UN MÉTODO -> Una clase derivada hereda todo lo que tiene una clase base. Pero también permite modificar el comportamiento de está herencia.
"""


class Droids:
    def encender(self):
        print("Encendido!")

    def apagar(self):
        print("Apagado!")


class otherDroid(Droids):
    def encender(self):
        print("Soy la clase HEREDADA!")


droids1 = Droids()
droids2 = otherDroid()

droids1.encender()
# Método heredado, pero sobreescrito!
droids2.encender()

"""
AÑADIR UN MÉTODO -> Añadir métodos que no estaban presentes en su clase base.
"""


class segundoDroide:
    def encender(self):
        print("Hola, en que te puedo ayudar")

    def apagar():
        print("Hola, estoy en descanso!")


class otroProtocoloDeDroid(segundoDroide):
    def encender(self):
        print("Hola, soy un droid de PROTOCOLO")

    def translate(self, msg, from_lang):
        return f'{msg} means "ZASCA" in {from_lang}'


robot1 = segundoDroide()
robot2 = otroProtocoloDeDroid()

print(robot2.translate("klitos", from_lang="Huttese"))


# ACCEDIENDO A LA CLASE BASE:
# Python ofrece la función super() para acceder a métodos o atributos de la clase base
class Droiden:
    def __init__(self, name):
        self.name = name


class otherDroiden(Droiden):
    def __init__(self, name, languages):
        # Llamada al constructor de la clase base
        super().__init__(name)
        self.languages = languages


droid = otherDroiden("C-3PO", ["Ewokese", "Huttese", "Jawase"])
# Fijado en la clase base y en la clase heredada
print(droid.name, droid.languages)

# HERENCIA MÚLTIPLE
# El orden en el que se específica la herencia múltiple es importante


class Droid:
    def greet(self):
        return "Here a droid"


class ProtocolDroid(Droid):
    def greet(self):
        return "Here a protocol droid"


class AstromechDroid(Droid):
    def greet(self):
        return "Here an astromech droid"


class SuperDroid(ProtocolDroid, AstromechDroid):
    pass


class HyperDroid(AstromechDroid, ProtocolDroid):
    pass


# Comprobar la herencia múltiple
print(issubclass(SuperDroid, (ProtocolDroid, AstromechDroid, Droid)))
print(issubclass(HyperDroid, (ProtocolDroid, AstromechDroid, Droid)))

super_droid = SuperDroid()
hyper_droid = HyperDroid()

print(super_droid.greet())
print(hyper_droid.greet())
