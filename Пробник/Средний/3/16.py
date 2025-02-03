from functools import lru_cache


@lru_cache
def f(n):
    if n <= 1:
        return n
    if n % 3 == 0:
        return f(n - 1) + f(n - 2) + 1
    return g(n - 3)


@lru_cache
def g(n):
    if n > 100:
        return n
    return g(n + 2) + 1


print(f(15) + f(12))