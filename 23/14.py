def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(int(bin(x)[2:] + '0', 2), y) + f(int(bin(x)[2:] + '1', 2), y)


print(f(int('100', 2), int('11101', 2)))