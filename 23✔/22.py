def f(x, y, k):
    if x > y:
        return 0
    if x == y and k == '*':
        return 1
    if k == '*':
        return f(x + 1, y, '*') + f(x + 2, y, '*')
    return f(x + 1, y, '+') + f(x + 2, y, '+') + f(x * 2, y, '*')


print(f(2, 12, '+'))
