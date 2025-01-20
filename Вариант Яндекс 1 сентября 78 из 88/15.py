def f(x, a):
    p = [y for y in range(64, 96)]
    q = [y for y in range(72, 107)]
    return  ((x in q) and (x not in a)) <= ((x not in p) <= (x not in q))


for a1 in range(1, 1000):
    for a2 in range(a1 + 1, 1000):
        if all([f(x, [y for y in range(a1, a2)]) for x in range(1, 100)]):
            print(len([y for y in range(a1, a2)]))