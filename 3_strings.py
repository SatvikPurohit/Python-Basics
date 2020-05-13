
# String
# 0-10
parrot = "Mithu-Mithu"
# h
print(parrot[3])
print()
# negative indexing: u
print(parrot[-7], parrot[10])
print()
# or h, 3 - string length
print(parrot[3 - 11])
print()

# Slice
print(parrot[:4], parrot[0:4], parrot, parrot[8:])
print()
print(parrot[:])
print()
# negative
print("negative ", parrot[-5:-3], parrot[-5:8])
print()
# steps
#                                start:stop:step
print(parrot[0::2], parrot[0::1], parrot[0:11:2])


# character , : range , :: step


# joins elements of list1 by '-'
# and stores in sting s
# elements have to be string
dob = "-".join(['2', '2', '1992'])
# join use to join a list of
# strings to a separator
print(dob)
print()

# reverse for
my_range = range(0,len(parrot))
print("type of " , type(range(0))," type of range obj ", type(my_range))
for char in range(0,len(parrot))[::-1]:
    print(parrot[char])
