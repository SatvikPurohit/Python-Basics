import sys


big_range = range(2000)

print("big range is of size {} bytes".format(sys.getsizeof(big_range)))

big_range_list = []

for n in big_range:
    big_range_list.append(n)

print("big range list is of size {} bytes".format(sys.getsizeof(big_range_list)))


print("int is of size {} bytes (OS specific)".format(sys.getsizeof(0)))

print()

# generator function


def my_range(n: int = 5):
    print("my range starts")
    start = 0
    while start < n:
        print("my range return {}".format(start))
        # return iterator
        yield start
        start += 1


my_range_var = my_range()

for i in my_range_var:
    print(i)

print("big range yield is of size {} bytes".format(sys.getsizeof(my_range_var)))
print("big range yield is of size {} bytes".format(sys.getsizeof(my_range_var)))


# 1000 records will be loaded in a memory
#  we can fetch one by one value
