from decimal import *
import time
from functools import wraps


def timeit_wrapper(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Alternatively, use time.process_time -- see the tutorial
        func_return_val = func(*args, **kwargs)
        end = time.perf_counter()
        print('{0:<10}.{1:<8} : {2:<8}'.format(func.__module__, func.__name__, end - start))
        return func_return_val

    return wrapper


@timeit_wrapper
def exp(x):
    """Raise e to the power of x.

    Algorithm taken verbatim from
    https://docs.python.org/3/library/decimal.html#recipes
    """
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s


if __name__ == '__main__':
    print('{0:<10}.{1:<8} : {2:<8}'.format('module', 'function', 'time'))
    exp(Decimal(150))
    exp(Decimal(400))
    exp(Decimal(3000))