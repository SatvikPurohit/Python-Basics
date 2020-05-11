from functools import reduce

num = [2, 3, 45, 6]

double = list(map(lambda e: e*2, num))
print("map ", double)

filtered = list(filter(lambda n: n is not 2, num))
print("filtered ", filtered)

# i + (i+1) elem
reduced = reduce(lambda n, i: n+i, double)
print("reduced ", reduced)
