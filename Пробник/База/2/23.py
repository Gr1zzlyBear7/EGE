def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(x + 3, y)


print(f(8, 28) * f(28, 31) * f(31, 43))