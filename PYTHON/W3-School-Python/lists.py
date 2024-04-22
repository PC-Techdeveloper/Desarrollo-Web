myList = ["apple", "banana", "cherry"]

print(myList)

print(len(myList))

# LIST ITEM - DATA TYPES

list1 = ["apple", "pear", "cherry"]
list2 = [1, 4, 6, 8]
list3 = [True, False]

print(list1)
print(list2)
print(list3)

print(type(list1))

# THE LIST CONSTRUCTOR -> list()
thisList = list(("apple", "banana", "cherry"))
print(thisList)

"""
ACCESS ITEMS
"""
print(thisList[1])
print(thisList[0:2])

"""
CHECK IF TIME EXISTS
"""
print("banana" in thisList)

"""
CHANGE ITEM VALUE
"""
thisList[0] = "pear"
thisList[2] = ["blackcurrant", "watermeion"]
print(thisList)

# Insert items
thisList.insert(2, "milk")
print(thisList)

"""
ADD LIST ITEMS - APPEND ITEMS
"""
# APPEND
lista = ["apple", "banana", "cherry"]
lista.append("orange")

# EXTEND -> You can add any iterable object (tuples, sets, dictionaries).
tropical = ["mango", "pineapple", "papaya"]
thisTuple = ("kiwi", "manzana")
lista.extend(thisTuple)
print(lista)

"""
REMOVE LIST ITEMS
"""
thisListTwo = ["apple", "manzana", "pear"]
thisListTwo.remove("apple")
print(thisListTwo)

# pop() -> Removes the specified index.
thisListTwo.pop(1)
print(thisListTwo)

del thisListTwo[0]
print(thisListTwo)

# Clear() -> Removes every of items
thisListTwo.clear()
print(thisListTwo)

"""
LOOP LIST FOR Y WHILE -> range(), len()
"""

# fruits = ["apple", "banana", "cherry"]

# for i in fruits:
#     print(i)

# for index, element in enumerate(fruits):
#     print(
#         f"EL índice es: {index} que corresponde al elemento {element} de la lista de frutas."
#     )

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# LOOPING USING LIST COMPREHENSIÓN -> SHORTHAND
# [print(x) for x in fruits]


"""
LIST COMPREHENSION -> List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
"""
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newList = []

# # Solo las frutas que contengan una 'a'
# for items in fruits:
#     if "a" in items:
#         newList.append(items)

# print(newList)


# List comprehension -> shorthand
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [item for item in fruits if item != "apple"]
# print(newlist)

# Iterable -> object, like a list, tuple, set, etc.
# newListTwo = [numbers for numbers in range(11)]
# print(newListTwo)

# WITH A CONDITION
newListThree = [numbers for numbers in range(10) if numbers < 5]
print(newListThree)

fruits = ["apple", "pear", "papaya", "lemon", "onion"]
fruitsUpper = [fruit.upper() for fruit in fruits]
print(fruitsUpper)

"""
SORT LIST -> A sort() method that will sort the list alphanumerically, ascending, by default 
"""
# SORT LIST ALPHANUMERICALLY

thisListThree = ["orange", "mango", "kiwi", "pineapple", "banana"]
listNumber = [100, 50, 65, 82, 23]

thisListThree.sort()
listNumber.sort()
print(thisListThree)
print(listNumber)

# SORT DESCENDING

thisListFour = ["mango", "orange", "kiwi", "pineapple"]
thisListFour.sort(reverse=True)
print(thisListFour)

listNumberTwo = [100, 50, 65, 82, 23]
listNumberTwo.sort(reverse=True)
print(listNumberTwo)

# CUSTOMIZE SORT FUNCTION


def myFunction(n):
    return abs(n - 50)


listNumberFive = [100, 50, 65, 82, 23]
listNumberFive.sort(key=myFunction)

print(listNumberFive)

# REVERSE ORDER
newThisList = ["banana", "Orange", "Kiwi", "cherry"]
newThisList.reverse()
print(newThisList)

# COPY LIST

newItems = ["apple", "banana", "cherry"]

newCopy = newItems.copy()

print(newItems)
print(newCopy)

# Make a copy of a list with the list() method.
newItemsTwo = ["apple", "banana", "cherry"]

myListCopy = list(newItemsTwo)
print(myListCopy)

"""
JOIN LIST -> There are several ways to join, or concatenate, two or more list in Python
"""

# Operator +
listOne = ["a", "b", "c"]
listTwo = [1, 2, 3]

listThree = listOne + listTwo
print(listThree)

# # With loop for

# for list in listTwo:
#     listOne.append(list)

# print(listOne)

# Use the extend() method
listOne.extend(listTwo)
print(listOne)

"""
LIST METHOD: 

append() -> Adds an element at the end of the list.
clear() -> Removes all the elements from the list.
copy() -> Returns a copy of the list.
count() -> Returns the number of elements with the specified value.
extend() -> Add the elements of a list (or any iterable), to the end of the current list.
index() -> Returns the index of the first element with the specified value.
insert() -> Adds an element at the specified position.
pop() -> Removes the element at the specified position.
remove() -> Removes the item with the specified value.
reverse() -> Reverses the order  of the list.
sort() -> Sorts the list.
"""
