myName = "My iterator"
print("My iterator")
myIter = iter(myName)
print(next(myIter))
print(next(myIter))
print()

# Combi exaple
print("iter(list), all nums bu next() then loop again")
nums = [1, 2, 3]
itru = iter(nums)
print(itru.__next__())
print(itru.__next__())
print(itru.__next__())
# Error
# print(itru.__next__())
print()

print("Now, Iter in loop")
for i in nums:
    print(i)


print()

# Own iterator
# Top Ten
# Override the methods


class TestIter:
    def __init__(self):
        super().__init__()
        self.num = 1
        self.name = "Satvik"

# as iter returns object
    def __iter__(self):
        return self

# as next returns value
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val, self.name
        else:
            # Or will keep giving None
            # Only way to stop for
            raise StopIteration


values = TestIter()
# 1
print(values.__next__())
# 2 to 10
for i in values:
    print(i)
