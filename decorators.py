# Decorators give extra functionality to our function, @ indicates the method is going to be used as decorator and a
# decorator should have a function as parameter, a wrap function and a return of that wrap function
def my_decorator(func):
    def wrap_func():
        print('************')
        func()
        print('************')

    return wrap_func


@my_decorator
def hello():
    print('Hello from Python')


hello()
print()


# Now a decorator with a wrap with parameters
def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('************')
        func(*args, **kwargs)
        print('************')

    return wrap_func


@my_decorator2
def hello2(x, y='=('):
    print(x, y)


hello2('Hello Xiurik')
