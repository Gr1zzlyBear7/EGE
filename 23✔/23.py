def f(x, y, k):
    if x > y:
        return 0
    elif x == y:
        return k <= 3
    return f(x + 2, y, k) + f(x * 3, y, k + 1) + f(x * 5, y, k + 1)


print(f(2, 200, 0))