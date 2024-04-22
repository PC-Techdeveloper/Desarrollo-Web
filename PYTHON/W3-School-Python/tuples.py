"""
PYTHON COLLECTIONS (ARRAYS) -> List, Tuple, Set, Dictionary

List -> Is a collections which is ordered and changeable.
Tuple -> Is a colletion which is ordered and unchangeable.
Set -> Is a collection whichs is unoredered, unchangeable.
Dictionary -> Is a collection which is ordered and changeable.

"""

# A tuple is a collection which is ordered and unchangeable.

myTuple = ("apple", "banana", "cherry")

print(myTuple)

# Tuple length
print(len(myTuple))

"""
TUPLE ITEMS - DATA TYPES
"""
tuple1 = ("apple", "orange", "pear")
tuple2 = (1, 5, 7, 8, 9)
tuple3 = (True, False, False)

# A tuple can contain different data types -> strings, integers and boolean
tuple4 = ("abc", 34, True, 40.5, "male")
print(type(tuple4))

# The tuple() constructor
thisTuple = tuple(("apple", "banana", "cherry", "onion", "melon", "kiwi"))
print(thisTuple)

"""
ACCES TUPLE ITEMS -> Index
"""
print(thisTuple[0])
print(thisTuple[-2])

"""
RANGE OF INDEXES
"""
print(thisTuple[2:5])
print(thisTuple[:4])
print(thisTuple[2:])
print(thisTuple[-4:-1])

"""
CHECK ITEMS
"""
if "melon" in thisTuple:
    print("Yes, 'melon' is in the fruits tuple!")

"""
UPDATE TUPLES
"""
# Convert the tuple into a list to be able to change it
firstTuple = ("melon", "lemon", "orange", "onion", "cherry")
secondTuple = list(firstTuple)

secondTuple[1] = "papaya"
print(secondTuple)

"""
ADD ITEMS
"""
myTupleOne = ("apple", "papaya", "lemon")
myTupleSecond = list(myTupleOne)

myTupleSecond.append("orange")

myTupleOne = tuple(myTupleSecond)

print(myTupleOne)

# ADD TUPLE TO A TUPLE
tuples1 = ("apple", "onion", "pear")

tuples2 = ("orange",)
tuples1 += tuples2

print(tuples1)

"""
REMOVE ITEMS
"""

thisTuple1 = ("apple", "banana", "cherry")
thisTuple2 = list(thisTuple1)
thisTuple2.remove("apple")
thisTuple1 = tuple(thisTuple2)

print(thisTuple1)


# The del keyword can delete the tuple completely
thisTuple1 = ("apple", "banana", "cherry")
del thisTuple1

"""
UNPACK TUPLES -> Extract the values back into variables. This is called 'unpacking'
"""

# The number of variables must match the number of values in the tuple.
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# USING ASTERISK -> *

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

"""
LOOP TUPLES
"""
tupla = ("mango", "papaya", "pineapple")

for items in tupla:
    print(items)

# Loop throught the index numbers -> range and len
for index in range(len(tupla)):
    print(tupla[index])

# Using a while loop
count = 0
while count < len(tupla):
    print(tupla[count])
    count += 1

"""
JOIN TWO TUPLES
"""
tupla1 = ("a", "b", "c")
tupla2 = (1, 2, 3)

tupla3 = tupla1 + tupla2
print(tupla3)

"""
MULTIPLY TUPLAS
"""
myFruits = ("apple", "banana", "cherry")
myTuples = myFruits * 2

print(myTuples)

"""
TUPLE METHODS: 

count() -> Returns the number of times a specified values occurs in a tuple
index() -> Searches the tuple for a specified values and returns the position of where it was found.
"""
