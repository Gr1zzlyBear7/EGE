def f(x, y, k):
    if x % 2 != 0:
        k += 1
    if x > y or k == 2:
        return 0
    if x == y:
        if k == 1:
            return 1
        return 0
    return f(x + 1, y, k) + f(x + 2, y, k) + f(x * 2, y, k)


print(f(2, 40, 0))