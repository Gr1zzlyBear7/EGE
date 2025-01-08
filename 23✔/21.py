def f(x, y, k):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif k == '*':
        return f(x + 1, y, '+') + f(x + 2, y, '+')
    return f(x + 1, y, '+') + f(x + 2, y, '+') + f(x * 2, y, '*')


print(f(1, 15, '+'))