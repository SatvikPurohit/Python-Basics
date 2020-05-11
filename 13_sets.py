# File  passed to interpreter
# /usr/bin/python3.6 /home/gslab/__Python/basics/13_sets.py

my_set = {"sheep", "Cow", "ghoda", "cow", "A", "a", "Cow"}
# Unordered - No duplicates!!!
print(my_set)
my_set.add("mindi")
print(my_set)
# {} means empty dictionary, so
new_set = set()
print(new_set)
num_set = set([1, 2, 3, 4])
print(num_set)
print()
print({1, 2, 3, 4}.union({5, 6, 7, 8}))
print({1, 2, 3, 4}.intersection({3, 4, 7, 8}))
print({1, 2, 3, 4}.intersection({3, 4, 7, 8}) == {3, 4})
print()
even = set(range(0, 20, 2))
# even.sort()
print(even)
print(sorted(even))
print()
print(" Difference ")
print({1, 2, 3}.difference({2, 4, 8}))
print({2, 4, 8} - {1, 2, 3})
# Pattern
# number = spaces = 3
# count = 0


# def pattern(spaces):
#     count
#     for i in range(0, spaces+1):
#         print(" ")
#         if(i == spaces):
#             count += 1
#             # number -= 1
#             print(count)
#             spaces -= 1
#             return pattern(spaces)


# pattern(spaces)
