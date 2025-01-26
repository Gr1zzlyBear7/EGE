def f(x, y):
    if x > y or x == 21:
        return 0
    if x == y:
        return 1
    if x % 2 == 0:
        return f(x + 1, y) + f(x + 4, y) + f(x + x + 2, y)
    return f(x + 1, y) + f(x + 4, y) + f(x + x + 1, y)


print(f(2, 11) * f(11, 26))
