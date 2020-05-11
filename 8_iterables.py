number = "9,223;334:448 223,432;123"
separators = ""

for separator in number:
    if not separator.isnumeric():
        separators = separators + separator

print(separators)
print()
for char in number:
    if char not in separators:
        print(char)
    else:
        print(" ")

print()

# slice start stop step
# range start stop step:incr/dec
for i in range(10, 15, 2):
    print(i)
print()
for i in range(15, 2, -1):
    print(i)

# While, while(condition) becomes false
print("While ")
i = 0
while(i < 10):
    print(i)
    if i == 2:
        break
    i += 1

print()

print("Auto iterable and iterable")
myName = "satvik"
for char in myName:
    print(char)

print()
ints = [1, 2, 3, 4, 5]
for idx, val in enumerate(ints):
    print(idx, val)
print()
