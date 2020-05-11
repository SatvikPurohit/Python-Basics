
# fibonacci
# first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string


def fibo(n):
    """Do nothing, but document it.
       No, really, it doesn't do anything.
       """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        # a = b
        # b = a+b
    print()


fibo(5)
print()

# The function inner uses three variables: aa, bb and cc. They're all different from Python's point of view: aa is lexically bound in outer, bb is locally bound in inner itself, and cc is not bound anywhere in sight, so it's treated as global.
# execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a global statement, or, for variables of enclosing functions, named in a nonlocal statement)

cc = 0


def outer(aa):
    def inner():
        bb = 1
        for i in range(0, 1):
            aa = 3
            cc = 3
            return aa + bb + cc
    return inner


print(outer(2), outer(2)())


a = 5


def function():
    a = 3
    print("Function", a)

    def func():
        a = 8
        print("Inner Function", a)
    print("Function", a)
    return func


f = function()
f()
print("Global ", a)

print()

name = 'Théo'


def change_name(new_name):
    name = new_name


print(name)

change_name('Karlijn')

print(name)
print()


def bob():
    global me
    me = "global defined"   # Defined locally but declared as global
    print(me)


bob()
print(me)     # Asking for a global variable

print()

foo = 1
count = 0


def test():
    foo = 2  # new local foo
    print("test foo ", foo)


def bulb():
    global foo
    print("bulb ", foo)
    foo += 3  # changes the value of the global foo
    print("bulb ", foo)
    # count += 1
    # while count < 2:
    #     count += 1
    #     print("count global ", count)
    while foo < 5:
        foo += 1
        print("count global ", foo)


test()
bulb()
print(foo)

print()

# non local
#


def out():
    x = "local"

    def inn():
        # Un comment
        # nonlocal x
        x = "nonlocal"
        print("inn:", x)

    inn()
    print("out:", x)


out()

print()


def my_name():
    print("my_name")


# Returns None
print(my_name())

# default argument


def return_my_name(my_name="Satvik"):
    return my_name


print(return_my_name(), return_my_name("Roma"), return_my_name("Loukik"))
print()

# default values are evaluated at the point of function definition
i = 5


def fu(arg=i):
    print(arg)


i = 6
fu()
print()

# default value is evaluated only once


def full(a, L=[]):
    L.append(a)
    return L


print(full(1))
print(full(2))
print(full(3))
print()

# solution


def fuk(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(fuk(1))
print(fuk(2))
print(fuk(3))
print()

# keyword args


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#  Invalid Arguments
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument, got multiple values for keyword argument
# parrot(actor='John Cleese')  # unknown keyword argument


# arguments keywords pointers
# When a final formal parameter of the form **name is present, it receives a dictionary
# formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.)
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print()
    for kw in keywords:
        print(kw, ":", keywords[kw])
    print()


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#


def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))

# lambda expression
# Small anonymous functions can be created with the lambda keyword
# just syntactic sugar for a normal functions
#  Lambda functions can be used wherever function objects are required


def make_incrementor(n):
    return lambda x: x + n


funky = make_incrementor(42)
print(" lambda executed ", funky(0))
print()

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

# if same name variable in function
#  still change global
test_var = '2'
print(test_var)


def funkykona():
    globals()['test_var'] = 3
    print(globals()['test_var'])
    test_var = 4
    print(test_var)


funkykona()
print(test_var)
print()


# recursion
def facto(n=4):
    if n == 0:
        return 1

    return n * facto(n-1)


print(facto())

# sum


def sum(n=4):
    if n == 0:
        # print(0)
        return 0
    if n == 1:
        # print(1)
        return 1

    return n + sum(n-1)


print(sum())


def fib(n: int, a: int = 0, b: int = 1):
    if (n < 0):
        return

    print(b)
    return fib(n - 1, b, a + b)

# stack
# 0 3 5
# 1 2 3
# 2 1 2
# 3 1 1
# 4 0 1


n: int = 4
fib(n)


# square
# square = lambda a:  a * a
# print(square(2))
