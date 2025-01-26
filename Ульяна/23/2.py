def fact(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1, y) + f(x + 4, y) + f(x + fact(x), y)


print(f(1, 10) * f(10, 20))