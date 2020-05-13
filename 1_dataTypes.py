# Dynamically and strongly Typed Language
# Python doesn't have compile-time type checking, so dynamically typed
A = "a"
print(type(A))
A = 12
print(type(A))
print()
def funcy():
    print()

print(type(funcy),"typ of function")
print()
# print(1 + 2 + 3 + "fu") Strongly Typed, TypeError

# Data types in Python:
# numeric, iterator, sequence, mapping, file, class, exception .... Type
# Python 3: int, float, complex, Decimal (for financial rounding) .... Class
print("Value")
a = 2
b = a
print("Value a and b <-- a ", a, b)
a = 3
print("Value changes b-->2 but ", a, b)
print()

print("unpacking , values can be lesser on either side but can't be grater")
y, space, z = "y z"
print(y, z)
print("common assignment ")
x = y = z = "yz"
print(x, y, z)
