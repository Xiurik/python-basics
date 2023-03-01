# Tuples: are like list that cant be modified once created, they are un-mutable, they can be used as list
# but cant be modified once created.
my_tuple = (1, 2, 3, 4, 5, 6, 6, 3, 4, 7, 3, 4, 8, 1, 3, 4, 7, 4, 3, 6)
print(my_tuple[3])

# We can also use Tuples in dictionaries as keys as Tuples are un-mutables
user = {"name": "Xiurik", (2, 6): "This is a Tuple"}
print(user[(2, 6)])
print()

# We can also use the slice, when the tuple only returns one single item, it will have at the end a ,
print("my_tuple[1:2] = ", my_tuple[1:2])

# If it returns more than a single item, it will show them normal
print("my_tuple[1:4] = ", my_tuple[1:4])

# Asign to variables
x, y, z, *other = (1, 2, 3, 4, 5, 6, 6, 3, 4, 7, 3, 4, 8, 1, 3, 4, 7, 4, 3, 6)
print("x,y,z", x, y, z)
print("other", other)
print()

# Count how many times a value is inside a tuple
print(f"The number 6 appears: {my_tuple.count(6)} times.")
print()

# Index is used to find the index of a value, if the value is repeated N times inside the tuple,
# it will return the index of the first match only
print(f"The index of 6 is: {my_tuple.index(6)}.")
print(f"The Tuple have {len(my_tuple)} items.")
