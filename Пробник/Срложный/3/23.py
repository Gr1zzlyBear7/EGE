def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x + 4, y)


for i in range(16, 1000):
    if f(15, i) == 4930:
        print(i)
        break