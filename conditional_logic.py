is_old = True
is_friend = True
is_licenced = True

# Normal IF
if is_old and is_licenced:
    print('Ok, we are inside the if True')
elif is_licenced:
    print('Ok, we are inside an elif (else if)')
else:
    print('Ok, we are inside an else')

# Ternary Operator or Conditional Expressions: used in special logic, is a sortcut to make the code more clean
msg_content = 'Hello Xiurik' if is_friend else 'Hello Sir, can you please attend my msg'

# Short Circuiting: Happens when one of the given validations is True and the compiler doesnt need to validate anything
# else, for example in an OR/AND statement
if is_old or is_friend:
    print('is_old is True so there is no need to validate is_friend')

is_old = False
if is_old and is_friend:
    print('is_old is False so there is no need to validate is_friend cause both need to be True')

if not is_old:
    print('We validate that is_old is equal to False')

# IS: used to validate that the values are exactly the same, type, value, etc and live in the same memory location,
# for example empty list are not the same cause they are created in a new location of memory

# This will be true cause we are validating the value
print(10 == 10.0)
# This will be False cause they are not the same type and value
print(10 is 10.0)
# This will be True cause they are exactly the same
print(10 is 10)
