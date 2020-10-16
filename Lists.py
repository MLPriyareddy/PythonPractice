Number=[1,"Priya", 2, 3, 4, "Anil", "Padma", 5]
print(Number[-1:-7:-2])

Number[1] = "Lakshmi"           # Changing specified index
print(Number)

Number.append("Boise")        # To add value at the end of the list
print(Number)

Number.insert(3, "Sri")        # To add value at specified index
print(Number)

Number.remove(2)              # To remove a value
print(Number)

Number.pop()                   # to remove last value
print(Number)

Number.pop(2)                # To remove specified value
print(Number)

del Number[1]                # To del specified index
print(Number)

Number.reverse()              # To reverse a list
print(Number)

Numbers = [1, 5, 3, 8, 4, 2, 6, 7]
Numbers.sort()                 # To sort the list
print(Numbers)

Number = [1, 3,"Priya", 4, 'Anil', 'Padma', 5]
if "Priya" in Number:
    print("Yes, Priya in the list")

# print(len(Number))
# x = Number.count(4)
# print(x)










