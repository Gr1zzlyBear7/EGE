from math import gcd


def f(x, a):
    return ((True if gcd(x, 42) != 1 else False) <= True if gcd(x, 7) == 1 else False) or (x + a >= 25)


for a in range(1, 1000):
    if all([f(x, a) for x in range(1, 10000)]):
        print(a)

