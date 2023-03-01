# Loops
# Iterable: is a collection that can be iterated [list, dictionary, tuple, set, string]
# Iterate: is going by one by to check each item in the collection

# For: allow us to iterate over anything that has a collection of items
data = [1, 2, 3, 4, 5, 6]
for el in data:
    print(el)

# Here outside the loop it will print the last value it had
print(el * 2)
print()

# For in a Dictionary: ways to iterate
user = {"name": "Irwin", "age": 50, "is_cool": True}

for el in user.items():
    print(el)
print()

for el in user.values():
    print(el)
print()

for el in user.keys():
    print(el)
print()

for key, value in user.items():
    print(f"KEY: {key}, VALUE: {value}")
print()

# Range: used to create a list with integers, we need to declare the start and end of the sequence,
# if no start is given, it will start in 0
# for d in range(1, 11):
#     print(d)
# print()

# You can use a variable or in case you dont need it we can use a _ and can be also used as a variable
for _ in range(1, 11):
    print("hello", _)
print()

# we can use a third parameter in the range to step over
for _ in range(0, 11, 2):
    print(_)
print()

# if we want to loop in reverse we can do it  with the -1
for _ in range(10, 0, -1):
    print(_)
print()

# we can use a third parameter in the range to step over also in reverse decreasing the -1 to -2,-3,-4, etc
for _ in range(10, 0, -2):
    print(_)
print()

for _ in range(0, 11):
    print(list(range(_)))
print()

# Enumerate: it will return a tuple with the index and value of each item, is very useful if you need the
# index counter of the item we are looping
for c in enumerate("Hello"):
    print(c)
print()

# unpacking a string
print("###### STRING - Hello ######")
for i, k in enumerate("Hello"):
    print(f"Index:{i}, Value:{k}")
print()

# unpacking a list
print("###### LIST - [1, 2, 3, 4, 5, 6] ######")
for i, k in enumerate([1, 2, 3, 4, 5, 6]):
    print(f"Index:{i}, Value:{k}")
print()

# unpacking a tuple
print("###### TUPLE - (1, 2, 3, 4) ######")
for i, k in enumerate((1, 2, 3, 4)):
    print(f"Index:{i}, Value:{k}")
print()

# Get the index of an specific value
for i, k in enumerate(list(range(100))):
    if i == 50:
        print(f"Index:{i} of value {k}")
print()

# Enumerate: it will return a tuple with the index and value of each item, is very useful if you need the
# index counter of the item we are looping
for c in enumerate("Hello"):
    print(c)
print()

# unpacking a string
print("###### STRING - Hello ######")
for i, k in enumerate("Hello"):
    print(f"Index:{i}, Value:{k}")
print()

# unpacking a list
print("###### LIST - [1, 2, 3, 4, 5, 6] ######")
for i, k in enumerate([1, 2, 3, 4, 5, 6]):
    print(f"Index:{i}, Value:{k}")
print()

# unpacking a tuple
print("###### TUPLE - (1, 2, 3, 4) ######")
for i, k in enumerate((1, 2, 3, 4)):
    print(f"Index:{i}, Value:{k}")
print()

# Get the index of an specific value
for i, k in enumerate(list(range(100))):
    if i == 50:
        print(f"Index:{i} of value {k}")
print()

# While: it loops while the condition is True
i = 1
while i <= 20:
    print(i)
    i += 1
# break
else:
    print("Done!")

print()

while True:
    response = input("Hello, how can I help you??")
    if str(response).upper() == "BYE":
        break
