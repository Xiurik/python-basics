# Best practices
# Should be snake_case
useriq = "this is wrong"
user_iq = "this is right"

# Start with lowercase or underscore
# Can be anything with letter, number or underscore
# Cant start with a number, only letters or underscore
like_this = None
_or_this = None

# Python is Case sensitive
this_is_one = None
this_Is_one = None

# Dont overwrite keywords
# List of keywords
# and - as - assert - break - class - continue - def - del - elif - else - except - False - finally - for - from -
# global - if - import - in - is - lambda - None - nonlocal - not - or - pass - raise - return - True - try - while -
# with - yield

# When we create a new variable from another, Python creates a new instance of it so we wont affect the original one
a1 = 120
b1 = a1
b1 += 1
print("a1 =", a1)
print("b1 =", b1)

# Constants are always in CAPITALS
NAME = "Xiurik"

# We should not create variable that start with double underscore __

# We can assigne values to multiple variables in one shot
# Statement: a, b, c = 1, 2, 'Hello' | Expression: 1, 2, 'Hello'
a, b, c = 1, 2, "Hello"
print("a:", a, "b:", b, "c:", c)

# Augmented assignment operator
# Junior Way
some_value = 8
some_value = some_value + 8
print(some_value)

# Using Augmented (PRO)
some_value += 8
print(some_value)
