"""
An iterator is an object that contains a countable number of values. An iterator is an object that can be  iterated upon, meaning that you can traverse throught all the values. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
"""

# ITERATOR VS ITERABLE: List, tuples, dictionaries and sets:

# Return an iterator from a tuple, and print each values:

myTuple = ("apple", "banana", "mango", "melon")
myIterator = iter(myTuple)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# Strings are also iterable, objects, containing a sequence of character

myString = "banana"

myIteratorTwo = iter(myString)

print(next(myIteratorTwo))
print(next(myIteratorTwo))
print(next(myIteratorTwo))
print(next(myIteratorTwo))
print(next(myIteratorTwo))
print(next(myIteratorTwo))

#  LOOPING THROUGHT AN ITERATOR:

myStringTwo = "mango"

for item in myStringTwo:
    print(item)

print()


# Create an iterator that returns numbers (returning 1,2,3,4,5, etc):


class MyNumbers:
    def __iter__(self):
        self.firstNumber = 1
        return self

    def __next__(self):
        numbers = self.firstNumber
        self.firstNumber += 1
        return numbers


myNums = MyNumbers()

myIterable = iter(myNums)
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))

print()

# Stop Iteration


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
