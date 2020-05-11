import shelve

# https://docs.python.org/3.7/library/functions.html
print("dir", dir())
# __builtins__ python builtin identifiers
for m in dir(__builtins__):
    # print(m)
    print('', end='')
print()
# __ __ not to change at all
# use shelve from output above
# shelve
print("shelve", dir(shelve))
for m in dir(shelve.Shelf):
    print(m)
    # print('', end='')
print(help(shelve))
# A “shelf” is a persistent, dictionary-like object. The difference with “dbm” databases is that the values (not the keys!) in a shelf can be essentially arbitrary Python objects — anything that the pickle module can handle. This includes most class instances, recursive data types, and objects containing lots of shared sub-objects.
