class Parent(object):
    def __init__(self, arg, *args, **kwargs):
        """ attributes """
        self.house_name = arg
        print("In Parent Init")

    def getHouseName(self):
        print("Parent house name, inherited ", self.house_name)


# By default will call to parent
# If child init is not there along with argument
# necessary for parent constructor


class Child(Parent):
    def __init__(self, arg, *args, **kwargs):
        super().__init__(arg, *args, **kwargs)
        print("In Child Init")

    def getHouseName(self):
        print("Child house name, inherited ", self.house_name)


class Sibling(Parent):
    def __init__(self, arg, *args, **kwargs):
        super().__init__(arg, *args, **kwargs)
        print("In Sibling Init")

    def getHouseName(self):
        print("Child house name, inherited ", self.house_name)

# class is inherited only from Child and not Sibling
# Left to Right


class GrandSon(Child, Sibling):
    def __init__(self, arg, *args, **kwargs):
        super().__init__(arg, *args, **kwargs)
        print("In GrandSon Init")

    def getHouseName(self):
        super().getHouseName()


grandSon = GrandSon("Satvalok")
print(grandSon.getHouseName())


class Base(object):
    def __init__(self, *args, **kwargs): pass


class A(Base):
    def __init__(self, *args, **kwargs):
        print("A")
        super(A, self).__init__(*args, **kwargs)


class B(Base):
    def __init__(self, *args, **kwargs):
        print("B")
        super(B, self).__init__(*args, **kwargs)


class C(A):
    def __init__(self, arg, *args, **kwargs):
        print("C", "arg=", arg)
        super(C, self).__init__(arg, *args, **kwargs)


class D(B):
    def __init__(self, arg, *args, **kwargs):
        print("D", "arg=", arg)
        super(D, self).__init__(arg, *args, **kwargs)


class E(C, D):
    def __init__(self, arg, *args, **kwargs):
        print("E", "arg=", arg)
        super(E, self).__init__(arg, *args, **kwargs)


print("Method Resolution Order")
for x in E.__mro__:
    print(x)
print("MRO Name arg ", [x.__name__ for x in E.__mro__])
E(10)
