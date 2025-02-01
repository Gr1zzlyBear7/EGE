def f(x, a):
    return ((x & 5160 > 0) or (x & 3650 > 0)) <= ((x & 9545 == 0) <= (x & a) > 0)


for a in range(7785, 10000):
    if all([f(x, a) for x in range(100000)]):
        print(a)
