# not
day = "Monday"
temp = 30
rain = True

if(day == "Saturday" and temp > 30 and not rain):
    print("Go swimming")
else:
    print("Learn Python")

if 0:
    print("True")
else:
    print("0 is False")


if "":
    print("True")
else:
    print(""""" is False""")

name = "Satvik"
letter = input("Please enter a letter: ")

if letter in name:
    print("{} is in {}".format(letter, name))
else:
    print("not in name")

if letter.casefold() not in name.casefold():
    print("not in name")
else:
    print("{} is in {}".format(letter, name))
