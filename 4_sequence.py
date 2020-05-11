# array strings
# String concat
print("Heyy " "Roma")
print()
print("Roma " * 5)
print(5 * " Roma")
print()

# print(1  + " Roma ") TypeError

# Replacement Field
print("1" + " Roma ")
print()
print(str(1) + " Roma ")
print()

# Three Sequence Types: list,tuples and range
print('Lists ')

numList = [1, 2, 3, 4, 5]
print("print using 'for in' ", numList)
for num in numList:
    print(num)
print()

numList.append(6)
print("append ", numList)
print()

numList2 = [7, 8, 9]
numList = numList2 + numList
print("Concat with '+' ", numList)
print()

numList.sort()
print("In place sort ", numList)
print()

sortedNumList = sorted((numList + [0]))
print("sort and return new ", sortedNumList)
print()

print(" Compare using '==' ", sortedNumList == numList)
print([1, 2, 3] == [1, 2, 3], [2, 3, 1] == [
      1, 2, 3], [1, 2, 3] == [1, 2], "** == **")
print()

list_1 = []
list_2 = list()

if list_1 == list_2:
    print('Use of List constructor list and list() and [] are equal ')
print()

print("Reference")
even = [2, 4, 6, 8]
odd = list(range(1, 10, 2))
print("odd after with 'range: range(1, 10, 2)'", odd)
another_even = even
print("whether contents are same after 'another_even = even'", another_even == even)
another_even.sort(reverse=True)
print("Refferring to same List so even changes if another_even is changed", even)
print()

print("No O(n^2)?")
binaryList = [[1, 1], [0, 1, 1, 1, 0], [
    0, 1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]]
print("Only List with 1's")
for numb in binaryList:
    if not 0 in numb:
        print(numb)
        for digit in numb:
            print(digit)

print()
# Python 2 Range was data type, now in 3 its function
small_decimals = range(1, 10)
print('Range will not return anything ', small_decimals)
print('but, "index" works, return index of number from range and not list of range --> ',
      small_decimals.index(3))
print('and number is "small_decimals[2]" --> ', small_decimals[2])
newSlice = small_decimals[::2]
print('also, "slice" works --> new list of odd ', list(newSlice))
print('range(0, 5, 2) == range(0, 6, 2) "equality" works --> without list ',
      range(0, 5, 2) == range(0, 6, 2))
print()
print(" reverse chunk of odd", list(newSlice[::-1]))
print("prints nothing")
for i in range(0, 100, -2):
    print("ulta")
print()

# List intended to hold items of same type
# Tuple was to hold heterogenius values and values that would not change

# Tuples: ordered set of data, like "immutable" list
#  with or without paranthesis ()
my_list_tuple = ['Kuni', 'pan yava', 'ani', 'tuple', 'marun java']
p, q, r, s, t = my_list_tuple
my_tuple = 'Kuni', 'pan yava', 'ani', 'tuple', 'marun java'
j, k, l, m, n = my_tuple
print(my_tuple, (1, 2, 34, 4))

print('my_*_tuple ')
my_list_tuple[3] = "Tupple"
print('work for list ', my_list_tuple)

print("so ")
t = ('275', '54000', '0.0', '5000.0', '0.0')
lst = list(t)
lst[0] = '300'
t = tuple(lst)
print("Modify a tuple", t)
print("OR")
t = t[:2] + (8, 9) + t[3:]
print("Modify a tuple 'Slicing' ", t)

# Error
print('Not work for tuple, "solution" --> new tupple')
my_tuple[3] = 'Tupple'
