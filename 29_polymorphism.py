from abc import ABC, abstractclassmethod

# Method Overloading
# Method Overriding
# Duck Typing
# Operator Overloading

# Duck Typing


class PyCharm:
    @staticmethod
    def execute():
        print("PyCharm")
        print("Compile")


class VsCode:
    @staticmethod
    def execute():
        print("VsCode")
        print("Format")
        print("Compile")


class Laptop:
    def code(self, ide):
        ide.execute()


py = PyCharm()
vs = VsCode()
lapy = Laptop()
lapy.code(py)
lapy.code(vs)


# 5 + "satvik"
# doesn't work
# Operator Overloading
# '+' operator's definition is __add__ (method) in python

class Students:
    def __init__(self, marks1):
        self.marks1 = marks1

    def __add__(self, other):
        return self.marks1 + other.marks1


s1 = Students(40)
s2 = Students(50)

sum = s1 + s2

print("sum ", sum)
a = 9
b = s1
print("9 number is ", a.__str__(), " similarly, s1 obj is ", b.__str__())
print()

# Method Overloading
#  Method Overriding


class A:
    def show(self):
        print("Hi in A")


class B(A):
    # pass
    # pass then A
    # else B
    def show(self):
        print("Hi in B")


b = B()
b.show()

# Absctract class
# can't instantiate
#  as no defined methods


class Computer:
    @abstractclassmethod
    def process(self):
        raise NotImplementedError

# If inherited we need to define
# NotImplemented even if one un-implemented
# enforcing inherited classes to implement those methods


class Laptop(Computer):
    def process(self):
        print("Yo man")


lapy = Laptop()
lapy.process()
