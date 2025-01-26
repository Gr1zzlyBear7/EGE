def f(x, y, k):
    if x > y or k == 2:
        return 0
    if x == y:
        return 1
    return f(x + 1, y, k + 1) + f(x + 3, y, 0) + f(x * 2, y, 0)


print(f(3, 30, 0))