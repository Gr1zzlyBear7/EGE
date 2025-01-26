def f(x, y):
    x = int(x, 2)
    y = int(y, 2)
    if x > y:
        return 0
    if x == y:
        return 1
    return f(bin(x + 1)[2:], bin(y)[2:]) + f(bin(x)[2:] + '0', bin(y)[2:]) + f(bin(x)[2:] + '1', bin(y)[2:])


print(f('101', '101110'))