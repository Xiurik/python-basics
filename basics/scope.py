# Scope: means what variables do I have access to??
# Rules #1: Start with local
# Rules #2: if not found in local, it goes to parent
# Rules #3: if nothing found it goes Global

# Global variables
total = 0


# GLOBAL: If we want to access to a global variable inside a function, we need to use global, example:
def return_total(n1, n2):
    global total
    total = n1 + n2


return_total(2, 8)
print(total)
print()


# NONLOCAL: is used to refer to parent local, it means we want to use the variable that is outside of the function,
# in this case the parent variable
def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner x:', x)

    inner()
    print('outer x:', x)


outer()
