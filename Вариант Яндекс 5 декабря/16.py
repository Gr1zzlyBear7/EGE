from functools import lru_cache
from sys import setrecursionlimit


setrecursionlimit(10000)


@lru_cache
def f(n):
    if n >= 2025:
        return 1
    return n - f(n + 2) - f(n + 4)


print(f(20) + f(25))