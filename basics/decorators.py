# Decorators give extra functionality to our function, @ indicates the method is going to be used as decorator and a
# decorator should have a function as parameter, a wrap function and a return of that wrap function
# Higher Order Function (HOC) - Is a function that accepts a function as a parameter or a function that returns a function

from time import time


def performance(fn):
    def wrap(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} s")
        return result

    return wrap


def my_decorator(func):
    def wrap_func():
        print("************")
        func()
        print("************")

    return wrap_func


@my_decorator
def hello():
    print("Hello from Python")


# hello()
# print()  # Prints a blank line


# Now a decorator with a wrap with parameters
def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print("************")
        func(*args, **kwargs)
        print("************")

    return wrap_func


@my_decorator2
def hello2(x, y="=|"):
    print(x, y)


# hello2('Hello Xiurik')
# print()


@performance
def long_time():
    for i in range(10000000):
        i * 5


# long_time()
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {"name": "Xiurik", "valid": False}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        print(args)
        if args and args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            print("no rights for this action")

    return wrapper


@authenticated
def message_friends(user, message):
    print("message has been sent")


message_friends(user1, "Hello")
