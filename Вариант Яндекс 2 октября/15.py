def f(x, y, a):
    return ((3 * x + y) > a) and (y < x) and (x < 30)


for a in range(1, 1000):
    arr = [f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)]
    if len(arr) == arr.count(False):
        print(a)

print()