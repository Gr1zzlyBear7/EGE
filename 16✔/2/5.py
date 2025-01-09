from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(100000)
def f(n):
    if n >= 10000:
        return n
    if n % 3 == 0:
        return n + f(n // 3)
    return 2 * n + f(n + 3)


print(f(999) - f(46))
