print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("B is greater then A")
else:
    print("B is not greater than A")

# EVALUATE VALUES AND VARIABLES
print(bool("Hello"))
print(bool(15))

# MOST VALUES ARE TRUE
# Any string, except empty string
# Any numbers, except 0
# Any list, set, and dictionary, except empty ones

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# SOME VALUES ARE FALSE
bool(False)
bool(None)
bool(0)
bool(2)
bool("")
bool(())
bool([])
bool({})


# Object
class myclass:
    def __len__(self):
        return 0


myObj = myclass()
print(bool(myObj))


# FUNCTIONS CAN RETURN A BOOLEAN
def myFunction():
    return True


# Invocando desde un condicional IF a una función
if myFunction():
    print("YES!")
else:
    print("NO!")

# CHECK IF AN OBJECT IS AN INTEGER OR NOT
x = 200
print(isinstance(x, int))
