# *args: is used to pass a variable number of arguments to a function. It is used to pass a non-key worded,
# variable-length argument tuple.
def args_function(*args):
    print(args)
    return sum(args)


print(args_function(1, 2, 3, 4, 5, 6))
print()


# **kwargs: is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star.
# The reason is because the double star allows us to pass through keyword arguments (and any number of them).
def kwargs_function(**kwargs):
    print(kwargs)
    total = 0
    for i in kwargs.values():
        total += i
    return total


print(kwargs_function(n1=1, n2=2, n3=3, n4=4, n5=5, n6=6))


# Rule: normal params, *args, default params, **kwargs, example:
def rule(def_param, *args, x=2, y=3, **kawargs):
    print('This is the rule, normal params, *args, default params, **kwargs')
