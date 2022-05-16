# Comprehensions (List, Set or Dictionary): provide us with a short and concise way to construct new sequences
# using sequences which have been already defined.

# List

# Without comprehensions
no_list = []
for item in 'HELLO':
    no_list.append(item)

# With comprehensions
with_list = [c for c in 'HELLO']
print(with_list)
print()

# Now lets get a list of 100 numbers
list_numbers = [i for i in range(1, 101)]
print(list_numbers)
print()

# Now lets get a list of 100 numbers by 2
list_numbers = [i * 2 for i in range(1, 101)]
print(list_numbers)
print()

# Now lets get a list of 100 numbers squared but only even
list_numbers = [i**2 for i in range(1, 101) if i % 2 == 0]
print(list_numbers)
print()

# Set
with_set = {c for c in 'HELLO'}
print(with_set)
print()

# Dictionary
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

diction_numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}

# dictionary of number and squared number
with_dict = {c: c**2 for c in numbers}
print(with_dict)
print()

# dictionary of number and cube numbers from a dictionary

with_dict = {c: v**2 for c, v in diction_numbers.items() if v % 2 == 0}
print(with_dict)
print()
