import functools

@functools.lru_cache
def f(x, y, s):
    if x > y:
        return 0
    elif s > 8:
        return 0
    elif x == y and s != 8:
        return 0
    elif x == y and s == 8:
        return 1
    return f(x + 1, y, s + 1) + f(x + 5, y, s + 1) + f(x * 3, y, s + 1)


k = 0
for i in range(1000, 1025):
    if f(1, i, 0):
        k += 1

print(k)
