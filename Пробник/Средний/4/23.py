def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(x + 3, y) + f(int(str(x) + '1'), y)


print(f(3, 12) * f(12, 25))