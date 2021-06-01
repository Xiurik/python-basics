# Normal Strings
user = 'hello'

# Long Strings starts with '''
long_string = '''
Hello
My Nigga
'''

print(long_string)

# Concatenation
name = "Xiurik"
last_name = 'The KING!'

print(name + str(5))

# Escape Sequence
# \t ==> adds a Tab
# \n ==> adds a new line
weather = "\t It\'s \"Kind of\" sunny \n\t and you know it baby"
print(weather)

# Formatted strings f''
name = 'Xiurik'
age = 30

print(f'Hello {name}, \nyou are {age} old man, congrats!')
print('Hello {}, \nyou are {} old man, congrats!'.format(name, age))
print('Hello {1}, \nyou are {0} old man, congrats!'.format(name, age))

# String Index
variable = '0123456789'
print(variable[2])

# [start:end]
print('[start:end] -->', variable[0:3])

# [start:end:step-over]
# Goes one by one
print('[start:end:stepover] -->', variable[0:6:1])
# Goes each 2
print('[start:end:stepover] -->', variable[0:6:2])

# [start:] - It will start on position 1
print('[start:] -->', variable[1:])

# [:number] - It will start on position 0 and stop in position 2
print('[:number] -->', variable[:2])

# start:end:step-over
# [::1] - It will start on position 1, : means default value
print('[::1] -->', variable[::1])

# [-1] - It will start on the last position, from right to left
print('[-1] -->', variable[-1])

# [::-1] - It will start on the last position, from right to left and show everything in reverse order
print('[::-1] -->', variable[::-1])

# Immutability, string values cannot be changed once created by Index
imm = '0123456789'

# this is correct
imm = 'hello'
# this is incorrect imm[3] = '4'

# string len starts on 1, not from 0 as usual
print(len('123456789'))

# String content format
the_value = 'hello my name is xiurik and xiurik likes to code'
print(the_value.upper())
print(the_value.capitalize())
print(the_value.lower())

# Find, tells you if the string have a specific word or letter and where it starts, in this example
# it tells me that my starts in position 6 of the string
print(the_value.find('my'))

# Replace, it will replace all the words or letters that match in the string
print(the_value.replace('xiurik', 'XAL'))
