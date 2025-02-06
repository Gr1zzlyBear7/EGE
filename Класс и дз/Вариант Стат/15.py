def f(x, a):
    return not (((x & 5160) > 0) or (x & 3650 > 0)) or ((x & 9545 != 0) or (x & a) > 0)


for a in range(6690, 10000):
    if all([f(x, a) for x in range(1000)]):
        print(a)
        break