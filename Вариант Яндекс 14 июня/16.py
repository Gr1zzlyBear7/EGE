from functools import lru_cache
import sys


sys.setrecursionlimit(10000)

@lru_cache(None)
def f(n):
    if n <= 1000:
        return n ** (n ** 2)
    if n > 1000:
        return n + 2 * f(n - 2) + 6 * f(n - 6)


for n in range(20024, -1, -1):
    f(n)

