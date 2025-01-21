def f(x, y, a):
    return (-(x - 2) ** 2 + 3 < y) or ((x - 1) ** 2 + y ** 2 < 7) or (5 * x + a > y)


for a in range(-100, 100):
    if all([f(x / 10, y / 10, a) for x in range(1, 100) for y in range(1, 100)]):
        print(a)
