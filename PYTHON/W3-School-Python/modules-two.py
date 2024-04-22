# SYNTAX: module_name.function_name.

import modules

modules.greeting("Jonathan")

# Import dictionary
data = modules.person1["age"]
print(data)

# Create an alis with 'as' -> called mx:
import modules as mx

name = mx.person1["name"]

print(name)

"""
BUILT-IN MODULES: There are several built-in modules in Python, which you can import whenever you like:
"""

# IMPORT AND USE THE PLATFORM MODULE:
import platform

x = platform.system()
print(x)

# USING DIR() FUNCTION: List all the defined names belonging to the platform module:
# x = dir(platform)
# print(x)

# IMPORT FROM MODULE: Using the 'from' keyword:
from modules import person2

print(person2["country"])
