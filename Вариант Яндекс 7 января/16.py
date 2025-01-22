from sys import *
from functools import *

setrecursionlimit(3000)
@lru_cache
def f(n):
    if n >= 2024:
        return 1
    return f(n + 2) + f(n + 4)

s = set()
for n in range(1, 20000):
    s.add(f(n))
print(len(s))