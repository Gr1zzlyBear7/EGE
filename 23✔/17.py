from functools import lru_cache


@lru_cache
def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 2, y) + f(x + 4, y) + f(x + 5, y)


for x in range(32, 1002):
    if f(31, x) == 1001:
        print(x)
