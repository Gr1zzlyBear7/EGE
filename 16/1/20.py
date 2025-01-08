import sys
from functools import lru_cache

sys.setrecursionlimit(3000)
@lru_cache
def f(n):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return f(n - 2) + n - 2
    return f(n + 2) + n + 2


k = 0

for i in range(1, 1000):
    try:
        if len(str(f(i))) == 5:
            k += 1
    except:
        pass

print(k)