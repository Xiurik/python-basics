# HOC (Higher Order Function) can be one of 2 things, it can be a function that accepts another function inside of
# its parameters, another is a function that returns another function.


# Case 1 (Examples are map, reduce)
def greet(func):
    func()


# Case 2
def greet2():

    def functionInside():
        return 6

    return functionInside
