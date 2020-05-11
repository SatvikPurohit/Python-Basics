#
name = input(" Please enter your name: ")
# By default expects string so wrap to get int
age = int(input(" Hi {0}, please enter your age: ".format(name)))

# and
if age >= 18:
    print("You can vote")
elif age < 18:
    print("You have to wait for {0} years to vote".format(18-age))
else:
    print("You can't vote")

print("*" * 25)

# and
if age >= 18 and age < 30:
    print("You are young")
# or
eat = input(" What do you like to eat? ")
if(eat == "Icecream" or eat == "Chocolate"):
    print("You are a foodie")
else:
    print("Go to Hell")
