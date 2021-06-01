# Set: Is an order collection of unique values, it will only return unique values without any duplicated value,
# it does not support indexing, is more like a dictionary
data = [1, 2, 3, 5, 6, 6, 4, 3, 1, 6, 7, 8, 9]
my_set = set(data)
my_set.add(10)  # Will be added
my_set.add(2)  # Wont be added cause already exist
print(my_set)
print(1 in my_set)
print()

# Convert the set to a list
print('set to list:', list(my_set))
print()

# We make a new copy of the set
new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)
print()

print('########################################################################')
print('############################ USEFUL METHODS ############################')
print('########################################################################')
outdated = {1, 2, 3, 4, 5, 6}
new_data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
new_data2 = {7, 8, 9, 10}
# Difference: useful to compare two sets and get the differences, in this example the values that new_data
# have but outdated doesnt
print('Difference:', new_data.difference(outdated))
print()

# Diacard: it will remove one value of the set, not by index, its by value itself
outdated.discard(5)
print('Diacard:', outdated)
print()

# Difference_update: It will remove all the values in new_data that exist in outdated and will remain
# only the values that does not exist in outdated.
# new_data.difference_update(outdated)
# print('Difference_update:', new_data)
# print()


print('outdated:', outdated)
print('new_data:', new_data)
print('new_data2:', new_data2)
print()

# Intersection: It will show you the values that both sets have
print('Intersection:', new_data.intersection(outdated))
print('Intersection:', new_data & outdated)

# IsDisJoint: Validate if the two sets have a null intersection
# False cause new_data and outdated have an intersection
print('IsDisJoint:', new_data.isdisjoint(outdated))
# True cause outdated and new_data2 doesnt have an intersection
print('IsDisJoint:', outdated.isdisjoint(new_data2))
print()

# IsSubSet: It will validate if the set contains the other set, in this case we ask if outdated exist in new_data
# This is True cause outdated exist in new_data
print('IsSubSet:', outdated.issubset(new_data))
# This is False cause new_data does not exist in outdated
print('IsSubSet:', new_data.issubset(outdated))
print()

# IsSuperSet: It will validate if the set contains the other set, same as IsSubSet but in the other way around,
# in this example we are validating if new_data contains outdated and more data to be a superset of outdated
print('IsSuperSet:', new_data.issuperset(outdated))
print()

# Union: it combines two sets and creates a new one without duplicates
print('Union:', new_data2.union(new_data))
print('Union:', new_data2 | new_data)
print()
