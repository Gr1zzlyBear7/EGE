from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000)


@lru_cache
def f(n):
    if n < 10:
        return n
    if n >= 10:
        return g(f(n - 1) % 10) + f(g(n % 10) - 1) - f(n - 3)


@lru_cache
def g(n):
    if n < 10:
        return -n
    if n >= 10:
        return f(g(n - 1) % 10) + g(f(n - 1) - 1) + g(n - 2)


print(f(1111) + g(1111))