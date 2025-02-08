from functools import lru_cache


@lru_cache
def f(n):
    if n < 10:
        return 0
    else:
        return f(n // 10) + (n // 10 % 10) - (n % 10)


k = 0
for n in range(0, 10**10):
    if f(n) == 9:
        k += 1
        print(k)
print(k)