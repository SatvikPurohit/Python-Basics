# Hash

alpha = {
    "a": "A",
    "b": "B",
    "c": "C",
    "q": "Q",
    "q": "kyu"
}

# TypeError: unhashable type
# beta = {
#     {}: "a"
# }
# print(beta)

if "a" in alpha:
    print(alpha["a"])
print()
for key in alpha:
    print("Key", key, "Value", alpha[key])
print()
print("Ordered Dict")
un_ordered_dict = {
    3: "Three",
    2: "Two",
    1: "One"
}
un_ordered_dict[4] = "Four"
print("Unordered ", un_ordered_dict)
# returns a list of all the values available in a given dictionary.
# the values have been stored in a reversed manner.
# dict_values
print("Unordered Values ", un_ordered_dict.values())
# dict_keys
ordered_keys = list(un_ordered_dict.keys())
ordered_keys.sort()
print("Ordered ", un_ordered_dict)
for key in ordered_keys:
    print(un_ordered_dict[key])
print()
# dict_items
un_ordered_dict_tuple = un_ordered_dict.items()
print("dict items --> tuple", un_ordered_dict_tuple)
print()
print("dic to tuple, by keys", tuple(un_ordered_dict))
print("tuple to dict ", dict(un_ordered_dict_tuple))
print()
delete = {
    "a": "A"
}
del delete["a"]
print("Delete by key ", delete)
print()
# Dict comprehension
string = "abcdefghi"
dict_comp = {k: v**3 for (k, v) in zip(string.ascii_lowercase, range(26))}
print("dict_comp ", dict_comp)
print()
# NameError: name 'delete' is not defined
del delete
print("Delete ", delete)
print()
