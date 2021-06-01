# This is a decorator to see how fast my code executes

from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'{func.__name__} took {round(t2 - t1, 2)} secs to run.')
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 6


long_time()
