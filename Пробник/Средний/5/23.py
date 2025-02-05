from functools import lru_cache


@lru_cache
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x + 4, y)


for n in range(16, 1000):
    if f(15, n) == 4930:
        print(n)
        break