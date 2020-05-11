import datetime
import pytz
# Everything in Python are object
# including variable and function
a = 10
b = 10
print(a.__add__(b))
print()
# when function is part of class it is called method
# else, function

# self =  this
# used to refer instance variable


class Kettle(object):
    power_source = "electricity"
    isAuth = "ISO"

    def __init__(self, make, price):
        """ attributes """
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        print(" ** object ** ", object)
        self.on = True


kerwood = Kettle("Kerwood", 0.99)
print(kerwood, " *** __main__ as its run from main** ")
print(kerwood, kerwood.make, kerwood.on, kerwood.price)
kerwood.price = 2.0
print("{0.price}".format(kerwood))
kerwood.switch_on()
print("kerwood {0.on}".format(kerwood))
lamp = Kettle("lamp", 0.90)
print("Lamp {0.on}".format(lamp))
lamp.power = "100h"
print("Lamp {0.power}".format(lamp))
print("class attribute to all instances (like static) ",
      kerwood.power_source, lamp.power_source)
print(kerwood.__dict__)
print()
print(lamp.__dict__)
print()
# Kettle.on: 'Kettle' has no attribute 'on'
print(Kettle.power_source)
print()
kerwood.power_source = "wood"
print("kerwood.__dict__", kerwood.__dict__,
      kerwood.power_source, lamp.power_source)
print("but ")
Kettle.power_source = "atomic"
print("2nd is instance 1st is attribute ",
      kerwood.power_source, lamp.power_source)
print("Class changes ",
      kerwood.isAuth, lamp.isAuth, end=' ')
Kettle.isAuth = "ISO9000"
print("--> ",
      kerwood.isAuth, lamp.isAuth)
print('##########################################')
print()


class Account:
    """ Simple account class with balance"""
# static variable
# can access with object or class name
# change , affects all objects
# as, its shared between all objects
# so class level or static variables
    type = 'savings'

    def __init__(self, name, balance):
        """
        Args:
            name: string

         """
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        print("Account created for ", name)

    @classmethod
    def info(cls):
        return cls.type

# independent logics are kept here
# things which have nothing to do with class variable or instance variable
    @staticmethod
    def _current_time():
        """ make it static as self is not used """
        dt = datetime.datetime.utcnow()
        return pytz.utc.localize(dt)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        self._transaction_list.append(
            (Account._current_time(), self.__balance))
        self.display()

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            self._transaction_list.append(
                (Account._current_time(), self.__balance))
        self.display()

    def display(self):
        for date, amount in self._transaction_list:
            if(amount > 0):
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
        print("{:6} {} on {} (local time was {})".format(
            amount, tran_type, date, date.astimezone()))

    # Object comparator
    def compare(self, obj):
        return self.__balance == obj.__balance


tim = Account("Tim", 100000)

tim.withdraw(100000)
tim.deposit(100000)

steph = Account("Steph", 100000)

# Object Equality
if steph == tim:
    print(" == ")
    print()
# actual way to compare
if steph.compare(tim):
    print(" .compare " "steph and tim are equal balance at this point")
print()
# class variable
print("access class variable or static variable", Account.type)
# classMethod, diffrent from static method
print(Account.info(),  " is the account type, using class method")
print()
# mangling:
# __  can't be changed
# '_Account__balance': 100000
# '__balance': 200
steph.__balance = 200
steph.withdraw(100000)
steph.deposit(100000)
print()
print("Steph ", steph.__dict__)
print()
help(Account.__init__.__doc__)
print()

#
print(id("satvik"))
print(id("satvik and Roma"))
print(id("satvik"))
