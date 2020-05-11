a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)   # float result
print(a // b)  # int division result
print(a % b)

# Arithmetic Rules

# precedence
print(a + b / 3 - 4 * 12)

# c = range(1, a//b)
# print(c + "*****")

print()

for i in range(1, 4):
    print(i)

# float division is not allowed
# for i in range(1, a/b):
    # print(i)

for i in range(1, a//b):
    print(i)
