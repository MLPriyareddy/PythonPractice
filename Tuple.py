mytuple = (1, "priya", 2, 3, 4, 5, 6)
print(mytuple)

# Accessing items

print(mytuple[1])
print(mytuple[-1])
print(mytuple[1:4])
print(mytuple[-6:-1])
print(mytuple[1:])
print(mytuple[:6])
print(mytuple[:-2])
print(mytuple[-3:])
print(mytuple[-1:-6:-2])



# we cannot add, change, remove a value to the tuple because tuples are immutable but we can do with the list.

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = list(tuple1)
tuple2.append(7)
tuple2.insert(8, 8)
tuple2[0] = 0
tuple2.insert(1, 1)
print(tuple2)
tuple1=tuple(tuple2)
print(tuple1)
print(len(tuple1))
y=tuple1.count(8)
print(y)

# To have only one item in tuple add comma
tuple3=("apple",)
print(tuple3)
x=tuple3.count("apple")
print(x)

# To know the type of tuple and count of items in the tuple
tuple4=("apple","apple")
print(type(tuple4))
z=tuple4.count("apple")
print(z)

# To delete tuple completly


try:
    tuple5 = ("orange", "apple", "grapes", "Guva")
    del tuple5                                                 # Tuple5 No longer exists
    print(tuple5)
except NameError:
    print("tuple5 no longer exists")



