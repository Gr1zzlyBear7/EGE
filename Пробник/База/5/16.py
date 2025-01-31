from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)


@lru_cache
def f(n):
    if n >= 7777:
        return n
    return n + 5 + f(n + 5)


for n in range(7777, 1000, -1):
    f(n)


print(f(1101) - f(1111))