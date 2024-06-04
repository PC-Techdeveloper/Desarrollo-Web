"""
PROGRAMA PRINCIPAL: Cuando se decide desarrollar una pieza de Software en Python, normalmente se usan ficheros para ello. Algunos de esos ficheros se convertirán en módulos, otros se englobarán en paquetes y existirá uno en concreto que será el punto de entrada, también llamado PROGRAMA PRINCIPAL.
"""

"""
La estructura es la siguiente:

- Importar de la librería estándar
- Importar de la librería de terceros
- Importar de módulos propios

- Código propio
...
- Código propio

if __name__ == "__main__":
  - Punto de entrada real

Para ejecutar este fichero desde la línea de comandos seria:

python main.py

Esta condición permite, en el programa principal, diferenciar que código se lanzará cuando el fichero se ejecute directamente o cuando el fichero se importe desde otro lugar

La variable __name__ toma los siguientes valores:
- El nombre del módulo (o paquete) al IMPORTAR el fichero.
- El valor __main__ al EJECUTAR el fichero.
"""

import hello

print(hello.myFunc())
