"""
READ FILES:

"r" -> Read: Default value. Opens a file for reading, error if the file does not exist
"a" -> Append: Opens a file for appending, creates the file if it does not exist
"w" -> Write: Opens a file for writing, creates the file if it does not exist
"x" -> Create: Creates the specified file, returns an error if the file exists
"t" -> Text: Default value. Text mode
"b" -> Binary: Binary mode (e.g. images)
"""

# SYNTAX: file = open("demofile.txt")

# file = open("demofile.txt", "r")
# print(file.read())

# OPEN A FILE ON A DIFFERENT LOCATION:
# file = open("D:\\myfiles\welcome.txt", "r")
# print(file.read())

# RETURN THE 5 FIRST CHARACTERS OF THE FILE
# file = open("demofile.txt", "r")
# print(file.read(5))
# print()

# READLINES -> READ ONE LINE OF THE LINE OR TWO LINES
# file = open("demofile.txt", "r")
# print(file.readline())
# print(file.readline())

# CLOSE FILES
# file = open("demofile.txt", "r")
# print(file.readline())
# file.close()

"""
FILE WRITE:

"a" -> Append: Will append to the end of the file
"w" -> Write: Will overwrite any existing content
"""

# PENDIENTE <--
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# Open the file "demofile2.txt" and append content to the file
f = open("demofile2.txt", "r")
print(f.read())

# Open the file "demofile3.txt" and overwrite thee content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# Open the read the file after the overwriting -> Deleted file
f = open("demofile3.txt", "r")
print(f.read())

"""
CREATE A NEW FILE: 

"x": Create: Will create a file, returns an error if the file exist
"a": Append: Will create a file if the specified file does not  exist
"w": Write: Will create a file if the specified file does not exist
"""
# A new empty file is created!
# f = open("myfile.txt", "x")

# Create a new file if it does not exist
# f = open("myfile.txt", "w")

"""
DELETE FILE: To delete a file, you must import the OS module, and run its os.remove() function:
"""

# Remove the file "demofile.txt"
import os

# os.remove("demofile.txt")

# Check if file exist:
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist!")

# DELETE FOLDER:

# To delete an entire folder, use the os.rmdir() method:
os.rmdir("myfolder")
