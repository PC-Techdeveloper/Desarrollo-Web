print("Hello")
print("Hello")

# ASSING STRING TO A VALUE
greeting = "Hello"
print(greeting)

# MULTILINE STRINGS
string1 = """
Lorem ipsum dolor sit amet,
consectetur adipscing elit, 
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

string2 = """
Lorem ipsum dolor sit amet,
consectetur adipscing elit, 
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(string2)

# STRING ARE ARRAYS
phrase = "Hello World!"
print(phrase[0], phrase[1])

print()

# LOOPING THROUGHT A STRING
for index in "banana":
    print(index)

# STRING LENGTH
string3 = "I am Developer"
print(len(string3))

# CHECK STRING -> You can use the keyword 'IN' -> returns a boolean value.
text = "The best things in life are free!"
print("free" in text)

# CHECK WITH CONDITIONAL IF
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# CHECK IF NOT -> You can use the keyword 'NOT'
txt = "The best things in life are free!"
print("expensive" not in txt)

# SLICING -> Slice

textOne = "Hello, World!"
print(textOne[0:3])
print(textOne[2:8])
print(textOne[:5])
print(textOne[2:])
print(textOne[-1:-5])

# MODIFY STRINGS

# UpperCase -> String in uuper case.
textTwo = "hello, python"
print(textTwo.upper())

# LowerCase -> String in lower case.
textThree = "HELLO, PYTHON!"
print(textThree.lower())

# REMOVE WHITESPACE

# strip() -> Removes any whitespace from the beginning or the end.
textFour = "  Hello, World!  "
print(textFour.strip())

# REPLACE STRING
print(textFour.replace("Hello", "Welcome to the "))

# SPLIT STRING
phrase = "Hello, World!"
print(phrase.split(","))

# STRING CONCATENATION
a = "Hello"
b = " World"
c = a + b
print(c)

d = "Hello"
e = "Robert"
f = d + " " + e
print(f)


# STRING FORMAT
age = 36
txt = "My name is John, I am {}".format(age)
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

# ESCAPE CHARACTER

# """
#  \ ' -> Single Quote
#  \ \ -> Backslash
#  \ n -> New Line
#  \ r -> Carriage Return
#  \ t -> Tab
#  \ b -> Backspace
#  \ f ->Form Feed
#  \ooo -> Octal value
#  \xhh -> Hex value

# """
TXT = 'We are the so-called "Vikings" from the north.'
print(TXT)


"""
METHOD STRINGS:

capitalize() -> Converts the first character to upper case.
casefold() -> Converts string into lower case.
center() -> Returns a centered string.
count() -> Returns the number of times a specified value occurs in a string.
encode -> Returns an encoded version of the string.
endsWith() -> Returns true if the string ends with the specified value.
expandtabs() -> Sets the tab size of the string.
find() -> Searches the string for a specified value and returns the position of where it was found.
format() -> Formats specified values in a string.
index() -> Searches the string for a specified value and returns the position of where it was found.
islanum() -> Returns True if all characters in the string are alphanumeric.
isascii() -> 	Returns True if all characters in the string are ascii characters.
isdecimal()	-> Returns True if all characters in the string are decimals.
isdigit()	-> Returns True if all characters in the string are digits.
isidentifier() -> Returns True if the string is an identifier.
islower()	-> Returns True if all characters in the string are lower case.
isnumeric()	-> Returns True if all characters in the string are numeric.
isprintable()	-> Returns True if all characters in the string are printable.
isspace()	-> Returns True if all characters in the string are whitespaces.
istitle()	-> Returns True if the string follows the rules of a title.
isupper()	-> Returns True if all characters in the string are upper case.
join() -> Converts the elements of an iterable into a string.
ljust()	-> Returns a left justified version of the string.
lower()	-> Converts a string into lower case.
lstrip()	-> Returns a left trim version of the string.
maketrans()	-> Returns a translation table to be used in translations.
partition()	-> Returns a tuple where the string is parted into three parts.
replace()	-> Returns a string where a specified value is replaced with a specified value.
rfind()	-> Searches the string for a specified value and returns the last position of where it was found.
rindex() -> Searches the string for a specified value and returns the last position of where it was found.
rjust()	-> Returns a right justified version of the string.
rpartition() -> Returns a tuple where the string is parted into three parts.
rsplit() -> Splits the string at the specified separator, and returns a list.
rstrip() -> Returns a right trim version of the string.
split()	-> Splits the string at the specified separator, and returns a list.
splitlines() -> Splits the string at line breaks and returns a list.
startswith() -> Returns true if the string starts with the specified value.
strip()	-> Returns a trimmed version of the string.
swapcase() -> Swaps cases, lower case becomes upper case and vice versa.
title()	-> Converts the first character of each word to upper case.
translate()	-> Returns a translated string.
upper()	-> Converts a string into upper case.
zfill()	-> Fills the string with a specified number of 0 values at the beginning.
"""
