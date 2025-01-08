from functools import lru_cache


@lru_cache
def f(n):
    if n <= 18:
        return n + 3
    if n % 3 == 0:
        return (n // 3) * f(n // 3) + n - 12
    return f(n - 1) + n ** 2 + 5


k = 0
for n in range(1, 1001):
    if all([True if int(x) % 2 == 0 else False for x in list(str(f(n)))]):
        k += 1
print(k)
