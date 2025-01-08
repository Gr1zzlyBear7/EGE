def count_f(n):
    count = 0
    for i in range(1, n):
        if f(i) == 3:
            count += 1
    return count

# Определяем функцию f
from functools import lru_cache

@lru_cache
def f(n):
    if n == 0:
        return 0
    if n % 2:
        return f(n - 1) + 1
    if n > 0 and n % 2 == 0:
        return f(n // 2)

# Подсчет значений
k = 0
for n in range(1, 1000000000):
    if f(n) == 3:
        k += 1

print(k)