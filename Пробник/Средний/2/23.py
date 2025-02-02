def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(x + sum(map(int, str(x))), y)


print(f(3, 29) * f(29, 68))