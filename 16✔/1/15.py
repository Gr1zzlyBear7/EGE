from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n / 2)
    return 1 + f(n - 1)


k = 0

for n in range(1, 501):
    if f(n) == 8:
        k += 1

print(k)