# Nested Functions
def sum1(n1, n2):
    def another_function(n11, n22):
        return n11 + n22

    return another_function(n1, n2)


total = sum1(10, 40)
print(total)
print()


# We can set functions to variables
def hello():
    print("Hello man")


greet = hello

# Here we delete hello name from function but not the method, so we can run it
del hello

print(greet())
print()


# We can also set an argument as function in a method
def hello2(func):
    func()
    return "Done"


def greetings():
    print("we are still alive")


a = hello2(greetings)

print(a)
print()
