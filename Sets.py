set1 = {"apple", "banana", "cherry", 1, "grapes", 2}

# We cannot access items because sets are unordered and not indexed.Can do with the loops

for x in set1:
    print(set1)

print("banana" in set1)

# we cannot change items in set1. we can add items to the set
# To add singe item
set1.add("orange")
print(set1)
# To add multiple items in  the set
set1.update([3, 4, 5])
print(set1)

# Length of the set
print(len(set1))

# To remove or discard a item
set1.remove(5)               # if the item does not exist it will raise an error
print(set1)
set1.discard(4)             # Will not raise an error if the item does not exist
print(set1)

print(len(set1))
set1.pop()                       # will not know which item will be deleted
print(set1)
