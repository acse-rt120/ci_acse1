from functools import lru_cache

__all__ = ['my_sum', 'factorial',"sum"]


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n-1) if n else 1


def sum(a,b):
    return a+b
