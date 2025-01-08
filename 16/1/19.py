import sys
from functools import lru_cache

sys.setrecursionlimit(3000)

@lru_cache
def f(n):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + f(n / 3)
    return n + f(n + 3)


for n in range(3, 1000, 3):
    try:
        if f(n) > 100:
            print(n)
            break
    except:
        pass