thisSet = {"apple", "banana", "cherry", True, 1, 2, 0}

print(thisSet)
print(type(thisSet))
# Get the length of a set
print(len(thisSet))

# THE SET() CONSTRUCTOR
thisSecondSet = set(("apple", "onion", "cherry", "orange"))

print(thisSecondSet)

"""
ACCESS ITEMS: Using a 'for' loop, or ask if a specified value is present in a set, by using the 'in' keyword
"""
for items in thisSecondSet:
    print(items)

# Check if a items is present in the set
print("onion" in thisSecondSet)

# Check if a items is NOT present in the set
print("cherry" not in thisSecondSet)

"""
ADD SET ITEMS: Once a sets is created, you cannot change its items, but you can add new items.
"""
thisSecondSet.add("lemon")
thisThirdSet = {"pineapple", "mango", "papaya"}
print(thisSecondSet)

# update() -> Add any iterable (list, set, dictionaries)
thisSecondSet.update(thisThirdSet)
print(thisSecondSet)

"""
REMOVE SET ITEMS: To remove an item in a set, use the remove(), or the discard() method.
"""
thisSecondSet.remove("lemon")
thisSecondSet.discard("apple")
thisSecondSet.pop()
thisSecondSet.clear()
print(thisSecondSet)


thisThirdSet = {"pineapple", "mango", "papaya"}
del thisThirdSet

"""
LOOP ITEMS: The set items by using a 'for' loop
"""
mySet = {1, 2, 3, 4, 5}

for element in mySet:
    print(element)

"""
JOIN SETS: 

1. The union() and update() methods joins all items from both sets.
2. The intersection() method keeps ONLY the duplicates.
3. The difference() method keeps the items from the first set that are not in the other sets.
4. The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

# Union() or use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)


# Join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


# update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# INTERSECTION or &
# Returns a new set, that only contains the items that are present in a both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# DIFFERENCE or -
# Return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2

print(set3)

# SIMMETRIC DIFFERENCES or ^
# Will keep only elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)


"""
SET METHODS:

add() -> Adds an element to the set.
clear() -> Removes all the elements from the set.
copy() -> Returns a copy of the set.
difference() OR (-)	-> Returns a set containing the difference between two or more sets
difference_update() OR (-=)	-> Removes the items in this set that are also included in another, specified set.
discard() -> Remove the specified item
intersection() OR (&) -> Returns a set, that is the intersection of two other sets.
intersection_update()	OR (&=)	-> Removes the items in this set that are not present in other, specified set(s).
isdisjoint() -> Returns whether two sets have a intersection or not.
issubset() OR (<=) -> Returns whether another set contains this set or not.
 	            (<)	Returns whether all items in this set is present in other, specified set(s)
issuperset() OR (>=)	Returns whether this set contains another set or not
 	            (>)	Returns whether all items in other, specified set(s) is present in this set.
pop() -> Removes an element from the set.
remove() -> Removes the specified element.
symmetric_difference() OR (^) -> Returns a set with the symmetric differences of two sets.
symmetric_difference_update()	OR (^=) -> Inserts the symmetric differences from this set and another
union()	OR (|) -> Return a set containing the union of sets.
update() OR (|=) -> Update the set with the union of this set and others.
"""
