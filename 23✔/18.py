from functools import lru_cache


@lru_cache
def f(x, y, s):
    if x > y:
        return 0
    elif x == y and s == 7:
        return 1
    elif x == y and s != 7:
        return 0
    return f(x + 1, y, s + 1) + f(x + 4, y, s + 1) + f(x * 2, y, s + 1)


print(f(3, 27, 0))


