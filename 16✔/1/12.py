from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return f(n - 1) - f(n - 2) + 3 * n


print(f(40))