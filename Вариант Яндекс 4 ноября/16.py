from functools import lru_cache

@lru_cache
def f(n):
    k = 1
    if n >= 1:
        k += 1
        k += f(n - 1)
        k += f(n // 2)
    return k


print(f(40))