def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    s = sum(list(map(int, str(x))))
    sq = int(str(x ** 2)[0])
    return f(x - sq, y) + f(x - s, y)


print(f(32, 1))