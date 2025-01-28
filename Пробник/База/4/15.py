def f(x, a):
    b = list(range(120, 131))
    return ((x in b) <= (x % 7 != 0)) or (a > (2 * x))


for a in range(1, 300):
    if all([f(x, a) for x in range(0, 10000)]):
        print(a)