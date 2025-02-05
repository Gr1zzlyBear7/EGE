from functools import lru_cache


@lru_cache()
def f(n):
    if n >= 2025:
        return n
    if n < 2025:
        return f(n + 1) - f(n + 2) + 7


for n in range(2025, 1, -1):
    f(n)
print(f(15) - f(24))