from functools import reduce

# Pure functions: A pure function is a function where the return value is only determined by its input values,
# without observable side effects. This is how functions in math work: Math.cos(x) will, for the same value of x,
# always return the same result.
numbers = [1, 2, 3, 4, 5, 6]
names = ['xiurik', 'jhon', 'fred', 'aaron', 'elena', 'ana', 'kate']


def multiply_by2(li):
    new_li = []
    for item in li:
        new_li.append(item * 2)
    return new_li


# print(multiply_by2(numbers))

# Map, filter, zip and reduce
# Map


def multiply_map(item):
    return item * 2


# To see the result we need to convert into a list, and we will have the same result as the first method
mapped = list(map(multiply_map, numbers))
print('MAP:', mapped)


# Filter
def check_odd(item):
    """
    Function to search the odd value
    """
    return item % 2 != 0


def search_name(item):
    """
    Function to search a name by specific value
    """
    valid = False
    if item.startswith('a'):
        valid = True

    return valid


filtered = list(filter(check_odd, numbers))
filtered_names = list(filter(search_name, names))
print('FILTER:', filtered)
print('FILTERED NAMES:', filtered_names)

# ZIP: we need 2 list or iterables to zip the together as tuples (can be as many list as we need)
# but only the same amount of items, if list1 have 20 and list2 have 30, it will only return 20 tuples
# the others are ignored
zipped = list(zip(numbers, names))
print('ZIPPED:', zipped)


# REDUCE: Allow us to reduce something by iteration, it will sum values with the last accumulator
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
# 15 + 6 = 21
def accumulator(acc, item):
    """
    A function to test REDUCE
    """
    return acc + item


reduced = reduce(accumulator, numbers, 0)
print('REDUCED:', reduced)
