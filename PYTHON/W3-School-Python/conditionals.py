"""
PYTHON CONDITIONS AND IF STATEMENTS:

Python support the usual logical conditions from mathematics:

==, !==, <, <=, >, >=
"""

# IF STATEMENTS:
a = 33
b = 200

if b > a:
    print("B is greater than A")

# ELIF STATEMENTS:
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# ELSE STATEMENTS:
a = 200
b = 33

if b > a:
    print("B is greater than A")
elif a == b:
    print("A and B are equal")
else:
    print("A is greater than B")


# SHORT HAND IF
if a > b:
    print("A is greater than B")

# SHORT HAND IF...ELSE
a = 2
b = 330

print("A") if a > b else print("B")

# CONDITIONALS EXPRESSIONS
a = 330
b = 550

print("A") if a > b else print("=") if a == b else print("B")

# Operator AND -> Lógical

a = 200
b = 55
c = 600

if a > b and c > a:
    print("Both conditions are True")

# Operator OR -> Lógical

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


# Operator NOT -> Lógical
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# NESTED IF
number = 41

if number > 10:
    print("Above ten,")
    if number > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


# THE PASS STATEMENT:

a = 33
b = 200

if b > a:
    pass
