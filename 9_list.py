shopping_list = ["milk", "pasta", "spam"]

# continue: skip everything after, and next iteration continues
# only easier to read
for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)
    print()

# break: breaks out of next iterations
for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)
    print()

# for index in range
# None, exist but its nothing ...  for better messages
# getting index outside for as well !!
found_at = None
for index in range(len(shopping_list)):
    if shopping_list[index] == "milk":
        found_at = index
        break
if found_at is not None:
    print("Found {} at {}".format(shopping_list[index], found_at))
else:
    print("Not found")
print()
# OR Without loop !!
item_to_find = "spam"
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
    print(item_to_find, "Found at: ",  str(found_at))

print()

# The basic syntax for list comprehensions is this: [EXPRESSION FOR ELEMENT IN SEQUENCE].
# A list comprehension creates an entire list in memory. at runtime
evenList = [x for x in range(10) if x % 2 == 0]
print(evenList)
