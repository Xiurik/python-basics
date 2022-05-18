# List slicing
# With slicing we create a new list of items
data_list = ['data0', 'data1', 'data2', 'data3', 'data4', 'data5', 'data6']

# Will show the first 2 items starting in position 0
print('[0:2] =', data_list[0:2])

# Will show all the items starting from position 0 but every 2
print('[0::2] =', data_list[0::2])

# Start in position 1 and stop in position 3, as we finish in position 3, position 3 wont show up
print('[1:3] =', data_list[1:3])

# Here we are telling that twin_list is whatever is in the memory of data_list, so both will always
# be equal when we change anything in one of them
print()
twin_list = data_list
twin_list[0] = 'changed'
print(data_list)
print(twin_list)

# But the correct way to make a new list from another is this one
print()
clone = data_list[:]
clone[0] = 'new value'
print(data_list)
print(clone)

# or using copy
print()
clone2 = data_list.copy()
clone2[0] = 'new value'
print(data_list)
print(clone2)

# Matrix: is a list with another lists inside
# This is a 2 dimensional list
matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [5, 7, 9],
]

# Here it goes to the first item in the list and get the position 1 of index
print(matrix[0][1])

# List Methods
basket = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Adding to the end of the list
basket.append(0)
print('append(0) : ', basket)
print()

# Adding into a specific index of the list (index,obj) | index starts on 0
basket.insert(3, 900)
print('insert(3, 900) : ', basket)
print()

# Add values to the end of the list, can be just one or more items
basket.extend([11, 12, 13, 14])
print('extend([11, 12, 13, 14]) : ', basket)
print()

# Removes the last item in the list
basket.pop()
print('pop() : ', basket)
print()

# Removes a specific item based on index
basket.pop(2)
print('pop(2) : ', basket)
print()

# Removes a specific value in the list (the first one found), we need to provide the value not the index
basket.remove(11)
print('remove(11) : ', basket)
print()

# Clears the whole list
basket.clear()
print('clear() : ', basket)
print()

# List Methods
basket_2 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', 'my', 'name', 'is', 'xiurik', 'xiurik', 'xiurik', 'xiurik', 'xiurik',
    'xiurik', 'xiurik', 'xiurik'
]

# Index, provide us the index of a specific value starting in 0
print(basket_2.index('my'))

# We can also provide the start and end position to look for the value in the index, it will start
# in the position X and stop before the position Y
x = 0
y = 10
print(basket_2.index('hello', x, y))

# Using keyword 'IN' to know if my is in basket_2, it will return a bool
print('name' in basket_2)
print('lo' in basket_2)

# Count will tell me how many times the value occurs in the list
print(basket_2.count('xiurik'))
print()

basket_str = [
    'darkrai',
    'riolu',
    'xiurik',
    'moltres',
    'articuno',
    'zapdos',
    'entei',
    'giratina',
    'dragonite',
    'pikachu',
    'gyarados',
    'genesect',
]
# Sort, it can only be applied to list with the same type of value
print('basket_str :', basket_str)
print()
basket_str.sort()
print('basket_str with sort :', basket_str)
print()

# Sorted create a new list sorted
new_basket = sorted(basket_str)
print('new_basket : ', new_basket)
print()

# Reverse switches the index of the items to show them from end to start but it will not sort the items, if we want
# them sorted we need to sort them first
new_basket.reverse()
print('new_basket with reverse: ', new_basket)
print()

# Another way to reverse and very commonly used is with slicing, it will also create a new list in return
print('reverse new_basket with slice [::-1]: ', new_basket[::-1])
print()

# range, very used to create a list and used in loops, for example from 1 to 99
new_range = list(range(1, 100))
print(new_range)
print()

# or the first from 0 to 100
new_range2 = list(range(101))
print(new_range2)
print()

# Join is used in strings, it will join all the items in a list with the value we provide,
# we combine a list with a string
sentence = '@?'.join(['hello', 'my', 'name', 'is', 'xiurik'])
print(sentence)
print()

# List Unpacking
a, b, c = [1, 2, 3]
print('a:', a, 'b:', b, 'c:', c)
print()

# We can also just create some variables and the last remain as a list with *VARIABLE
d, e, *the_list = [1, 2, 3, 4, 5, 6]
print('d:', d, 'e:', e, 'the_list:', the_list)
print()

# We can also assign the list specific amount of values setting up after the list the remaining variables we want
f, g, *the_list, h = [1, 2, 3, 4, 5, 6]
print('f:', f, 'g:', g, 'the_list:', the_list, 'h:', h)
print()
