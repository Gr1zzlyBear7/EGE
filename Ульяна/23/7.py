def f(x, y, k):
    if x > y:
        return 0
    if x == y:
        return 1
    if k == 'B':
        return f(x + 2, y, 'A') + f(x * 3, y, 'C')
    return f(x + 2, y, 'A') + f(x ** 2, y, 'B') + f(x * 3, y, 'c')

print(f(2, 64, 0))