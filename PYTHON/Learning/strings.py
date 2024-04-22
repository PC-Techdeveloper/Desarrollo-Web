# Conatenar strings

first_name = "Asabeneh"
last_name = " Yetayeh"
language = "Python"
full_name = first_name + last_name
print(full_name)
"""
SECUENCIAS DE ESCAPE
\n -> Saltos de línea.
\t -> Tabulador.
\\ -> Barra invertida.
\' -> Comillas simples.
\" -> Comillas dobles.
"""

"""
FORMATEAR TEXTO -> MANERA ANTIGUA
%s -> Cadenas de texto
%d -> Números enteros
%f -> Números flotantes
%. -> Números flotantes con presición fija
FORMATEAR TEXTO -> FORMA NUEVA
{} -> Plantillas literales -> MÁS USADA
.format -> Colocar las variables
"""
# %s -> strings
formatear_texto = "Yo soy %s %s. I teach %s" % (first_name, last_name, language)
print(formatear_texto)

# %d -> Números enteros.
radio = 10
pi = 3.14
area = pi * radio**2
formatear_numeros = "El área del círculo con radio %d es %.2f" % (radio, area)
print(formatear_numeros)

# Nueva forma de formatear texto -> Menos usada
print("I am {} {}. I teach {}".format(first_name, last_name, language))

# Nueva forma de formatear texto -> Más utilizada y recomendable
# Más conocido como la interpolación de texto, ya que empieza con f"...{}"
print(f"El área del círculo es: {area:.2f}")

"""
DESEMPAQUETADO DE CARÁCTERES -> Extraer un carater
"""
lenguaje = "Python"
a, b, c, d, e, f = lenguaje
print(a)
print(c)

"""
ACCEDER A LOS CARÁCTERES POR ÍNDICE -> Comienza desde 0, valores negativos desde -1, -2...
"""
print(lenguaje[0])
print(lenguaje[1])
print(lenguaje[-1])
print(lenguaje[-2])

"""
SLICING O REBANAR CARÁCTERES -> Subcadenas rebanadas.
SALTAR CARÁCTERES MIENTRAS SE CORTA -> Omitir carácteres mientras se corta
"""
print(lenguaje[0:2])
print(lenguaje[2:])
print(lenguaje[:-2])

# Invertir string
print(lenguaje[::-1])

# Skiping of strings
print(lenguaje[0:6:2])

"""
STRING METHODS
"""
# capitalize -> Primer letra en mayúscula
challengue = "30 dias de python"
sub_cadena = "da"
print(challengue.capitalize())

# count -> Cuenta cuantas veces se repite una subcadena
print(challengue.count("d"))

# startswith -> Verifica si comienza por...
print(challengue.startswith("on"))

# endswith -> Verifica si la termina en...
print(challengue.endswith("on"))

# expandtabs -> Reemplaza la tabulación del carácter con espacios
print(challengue.expandtabs(5))

# find -> Retorna el índice de la ocurrencia de una subcadena
print(challengue.find("d"))

# rfind -> Retorna el último índice de la ocurrencia de una subcadena
print(challengue.rfind("th"))

# format -> Formatea el texto por salida
print("Challengue: {}".format(challengue))

# index -> Retorna el índice más bajo de una subcadena
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))

# rindex -> Retorna el índice más alto de una subcadena
challenge = "thirty days of python"
sub_string = "da"
print(challenge.rindex(sub_string))

# lower -> Subcadena en minúscula
# upper -> Subcadena en mayúscula
print(first_name.upper())
first_name2 = "ROGER"
print(first_name2.lower())

# join -> Retorna una concatenación de un string
web_tech = ["HTML", "CSS", "JAVASCRIPT", "REACT"]
resultado = "#".join(web_tech)
print(resultado)

# strip -> Elimina todos los caracteres dados comenzando desde el principio y el final de la cadena.
print(challenge.strip("thon"))

# replace -> Reemplazar una subcadena por otra nueva
print(challenge.replace("python", "javascript"))

# split -> Divide la cadena, usando una cadena o espacio dado como separador
challenge2 = "thirty days of angular"
print(challenge2.split(", "))

# title -> Retorna todas las primeras letras en mayúscula
print(challenge2.title())

# swapcase -> Retorna todos los carácteres en mayúscula y minúscula
challenge3 = "Thirty Days Of React"
print(challenge3.swapcase())
