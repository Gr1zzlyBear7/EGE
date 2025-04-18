def f(x, y, a):
    return (5 < y) or (x > 32) or (x + 2 * y < a)


for a in range(0, 100):
    if all([f(x, y, a) for x in range(100) for y in range(100)]):
        print(a)