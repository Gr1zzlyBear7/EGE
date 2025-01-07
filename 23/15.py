def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(int(''.join([str(x + 1) if x != 9 else str(x) for x in list(map(int, str(x)))])), y)


print(f(25, 51))
