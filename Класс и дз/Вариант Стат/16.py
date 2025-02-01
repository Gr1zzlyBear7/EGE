from functools import *


@lru_cache
def f(n):
    if n == 0:
        return 0
    if n % 4 < 2 and n > 0:
        return f(n // 4) + n % 4
    if n % 4 >= 2:
        return f(n // 4) + abs(n % 4) - 1


for n in range(100):
    f(n)
for n in range(100):
    if f(n) == 27 and f(n + 1) == 16:
        print(n)

