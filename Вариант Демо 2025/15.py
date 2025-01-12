p = [x for x in range(15, 41)]
q = [x for x in range(21, 64)]


def f(x, a):
    return (x in p) <= (((x in q) and (x not in a)) <= (x not in p))


k = 0
for a in range(1, 100):
    if all([f(x, [s for s in range(1, a + 1)]) for x in range(100)]):
        print(a)
        break