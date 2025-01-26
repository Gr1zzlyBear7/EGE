def f(x, y, k):
    if x > y or k == 3:
        return 0
    if x == y:
        return 1
    return f(x + 1, y, k) + f(x + 2, y, k) + f(x * 2, y, k + 1)


print(f(2, 12, 0))
