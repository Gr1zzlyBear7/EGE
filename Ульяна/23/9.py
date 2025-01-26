def f(x, y, k):
    if x > y or k == 3:
        return 0
    if x == y:
        return 1
    return f(x - 2, y, k + 1) + f(x * 3, y, k) + f(x * 2, y, k)


print(f(6, 48, 0))