from functools import lru_cache


@lru_cache
def f(n):
    if n < 13:
        return 13
    if abs(n) % 5:
        return 13 - f(n - 1)
    return 13 + f(n - 1)


for n in range(3015):
    f(n)
print(f(3013))