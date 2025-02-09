from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(30000)

@lru_cache
def f(n):
    if n == 1:
        return 1
    else:
        return (n - 1) * f(n - 1)


for n in range(2000):
    f(n)