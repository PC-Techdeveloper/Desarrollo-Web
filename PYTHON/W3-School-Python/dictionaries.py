"""
ACCESS DICTIONARY ITEMS: 
"""

thisDict = {"brand": "Ford", "model": "Mustang", "year": 1934}

print(thisDict["brand"])

myDict = thisDict.get("model")
print(myDict)

# GET KEYS
print(thisDict.keys())

# GET VALUES
print(thisDict.values())

# GET ITEMS
print(thisDict.items())

# CHECK IF KEY EXISTS
if "year" in thisDict:
    print("Yes, 'year' is one of the keys in the thisDict dictionary.")

"""
CHANGE ITEMS: 
"""

thisDict["year"] = 2020
print(thisDict)

# UPDATE DICTIONARY
thisDict.update({"year": 2024})

print(thisDict)

# ADDING ITEMS
thisDict["color"] = "red"
print(thisDict)

thisDict.update({"color": "blue"})
print(thisDict)

"""
REMOVING ITEMS:
"""
# pop() method removes the item with the specified key name:
thisDict.pop("model")
print(thisDict)

# popitem() method removes the last inserted item, a random item is removed instead:
print(thisDict.popitem())

thisDictTwo = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisDictTwo["model"]
print(thisDictTwo)

# the clear() method empties the dictionary:

thisDictTwo.clear()
print(thisDictTwo)


"""
LOOP DICTIONARIES: 'for' loop
"""

for elements in thisDict:
    print(elements)

# Print all values in the dictionary, one by one

for values in thisDict:
    print(thisDict[values])

# method keys, values, items with for loop
for values in thisDict.values():
    print(values)

"""
COPY DICTIONARY: There are ways to make a copy, one way is to use the built-in Dictionary method method copy().
"""

# Make a copy a dictionary with the copy() method:
myDictTwo = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(myDictTwo)

# Make a copy a dictionary with the dict() function:
print(dict(myDictTwo))

"""
NESTED DICTIONARIES: A dictionary can contain dictionaries, this is called nested dictionaries.
"""

myFamily = {
    "childOne": {
        "name": "Emil",
        "year": 2004,
    },
    "childTwo": {
        "name": "John",
        "year": 2007,
    },
    "childThree": {"name": "Maria", "year": 2011},
}

print(myFamily)

# Or created three dictionaries into new dictionary:
child1 = {
    "name": "Emil",
    "year": 2004,
}
child2 = {
    "name": "John",
    "year": 2007,
}
child3 = ({"name": "Maria", "year": 2011},)

myFamilyTwo = {"child1": child1, "child2": child2, "child3": child3}

print(myFamilyTwo)

# ACCESS ITEMS IN NESTED DICTIONARIES:
print(myFamilyTwo["child2"]["name"])
print(myFamilyTwo["child2"]["year"])

print()

# LOOP THROUGHT NESTED DICTIONARIES:
for element, obj in myFamily.items():
    print(element)

    for elementTwo in obj:
        print(f"{elementTwo}: {obj[elementTwo]}")

"""
DICTIONARIEY METHODS:

clear() -> Removes all the elements from the dictionary.
copy() -> Returns a copy of the dictionary.
fromkeys() -> Returns a dictionary with the specified keys and value.
get() -> Returns the value of the specified key.
items() -> Returns a list containing a tuple for each key value pair.
keys() -> Returns a list containing the dictionary's keys.
pop() -> Removes the element with the specified key.
popitem() -> Removes the last inserted key-value pair.
setdefault() -> Returns the value of the specified key. If the key does not exist: insert the key, with the specified value.
update() -> Updates the dictionary with the specified key-value pairs.
values() -> Returns a list of all the values in the dictionary.
"""
