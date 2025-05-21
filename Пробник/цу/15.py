def f(x, a):
    return ((x % 2 == 0) <= (x % 5 != 0)) or (x + a >= 90)


for a in range(1, 1000):
    if all([f(x, a) for x in range(1, 10000)]):
        print(a)