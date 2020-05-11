# Input needs to be sorted
# list.sort sorts the list in place, i.e. it doesn't return a new list
# .sort wont work
import random
num_list = [2, 5, 1, 3, 6, 7, 100, 20, 49]
num_list = sorted(num_list)

toBeSearched = 5
# toBeSearched, middle, lower_bound index, upper_bound index, array of numbers
# index of number to be searched


def binary_search(arr, l, u):
    if u >= l:
        m = l + ((u-l)//2)
        if num_list[m] == toBeSearched:
            return m
        elif num_list[m] > toBeSearched:
            return binary_search(arr, l, m-1)
        else:
            return binary_search(arr, m+1, u)
    else:
        return -1


answer = binary_search(num_list, 0, (len(num_list)-1))

print(answer)
print()

print("Binary search implimentation ")
print("Guess the number between 1 to 1000 in your mind ")
guess = None
r = 1000
l = 1
count = 0


def guesses(l, r):
    global count
    #
    if(r >= l):
        while True:
            guess = l + ((r-l)//2)
            count += 1
            print("My guess is {} ".format(guess))
            print(
                "Press keys c to Confirm answer, h to guess Higher answer and l to guess Lower answer ")
            key = input().casefold()
            if key == 'h':
                # guesses(guess+1, r)
                return guesses(guess+1, r)
            elif key == 'l':
                # guesses(l, guess-1)
                return guesses(l, guess-1)
            else:
                print("Total number of guess were {}".format(count))
                break
    else:
        pass


guesses(l, r)
print()
