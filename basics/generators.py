from time import time

# Generatos: Allow us to generate a sequence of values over time like range(1000)
# they dont hold things in memory, instead, they process data efficiently
# they are useful when calculating large sets of data particularly if we are using
# long loops where we don't really want to store that memory and we dont need to
# calculate everything at the same time.
"""
def generator_function(num):
    for i in range(num):
        # yield is a keyword that tells Python to return the value
        # it pauses the function and comes back when we do something or we call next
        yield i * 2


g = generator_function(10)
next(g)  # the first item is 0, so is 0x2=0
next(g)  # the next item is 1, so is 1x2=2
print(next(g))  # the next item is 2, so is 2x2=4

for i in generator_function(10):
    print(i)
    
"""

###################################################################
############# Compare performance with Range and List #############
###################################################################
"""
def performance(fn):

    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} seconds')
        return result

    return wrapper


@performance
def ltrange():
    print('Doing with range')
    for i in range(1000000):
        i * 5


@performance
def ltlist():
    print('Doing with list')
    for i in list(range(1000000)):
        i * 5


ltrange()
ltlist()
"""

####################################################################
################ How generators work under the hood ################
####################################################################
"""
class myGenerator():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if myGenerator.current < self.last:
            num = myGenerator.current
            myGenerator.current += 1
            return num
        raise StopIteration


gen = myGenerator(0, 10)
for i in gen:
    print(i)
"""

###################################################################
######################## Fibonacci Numbers ########################
###################################################################


def genFibonacci(num):
    f1 = 0
    f2 = 1
    for i in range(num):
        yield f1
        temp = f1
        f1 = f2
        f2 = temp + f2
        print(temp, f1, f2)


for i in genFibonacci(20):
    print(i)
