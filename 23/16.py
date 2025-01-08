def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + (f(x * 1.5, y) if x % 2 == 0 else 0)


print(f(1, 20))