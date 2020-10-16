dict1 = {"Name": "Priya",
         "city": "Boise",
         "zipcode": 83709,
         "state": "Idaho",
         "AreaCode": 208
         }
# Accessing items by using key value
x = dict1["zipcode"]
print(x)
y=dict1.get("zipcode")
print(y)
# Change Values
dict1["city"] = "Meridian"
print(dict1)

# loop through
for x in dict1:                            # Print all key values one by one
    print(x)

for i in dict1:                            # Print all values one by one
    print(dict1[i])
     # OR
for z in dict1.values():
    print(z)

for k,j in dict1.items():                      # Key:Value
    print(k,j)

if "Name" in dict1:
    print("Yes")

print(len(dict1))

# Adding items
dict1["car"] = "VW"
print(dict1)

# Remove an item
dict1.pop("AreaCode")         # Removes specified key
print(dict1)

dict1.popitem()
print(dict1)

print(len(dict1))
print(abs(-203))