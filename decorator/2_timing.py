# Practical Example of Decorator #2 - Timing

import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute!")
        return value

    return wrapper


@timed
def add(x, y):
    time.sleep(2)
    return x + y


print(add(1, 2))
