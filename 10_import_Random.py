import random

answer = random.randint(1, 10)
print("Please guess the number between 1-10")
guess = int(input())
# print("Random num: ", str(answer), str(guess))
if answer == guess:
    print("You got it right first time")
else:
    while (answer != guess):
        if answer > guess:
            print(" guess slightly higher number ")
        else:
            print(" guess slightly lower number ")
        guess = int(input())
    print("You guessed it right, answer is {}".format(guess))
print()
print(5//2)
