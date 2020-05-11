print("{0} Roma ".format(1))
print("{0} {1} {2} Roma ".format(1, 2, 3))
print("{0} {1} {0} Roma ".format(1, 2, 3))
print((1 + 5) * " Roma ")
# in op
print("day" in "Today")
# formating by adding width
for i in range(1, 13):
    print("No. {0:2}, sqr is {1:3}, cube is {2:4}".format(i, i**2, i**3))
# left align <, ^ center, by default right aligned (space to left)
for i in range(1, 13):
    print("No. {0:<2} sqr is {1:^3} cube is {2:<4}".format(i, i**2, i**3))

print()
print("Pi is {0:2.4f}".format(22/7))
print()
# v greater than 3.4 only
print(f"Pi is {22/7:2.3f}")
# v 2 interpolation not in 3
print("Pi is %d" % (22/7))
print("Pi is %f" % (22/7))
print("%s is %.4f" % ("Pi", 22/7))
