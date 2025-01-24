from math import gcd


def f(x, a):
    return (1 != gcd(x, 42)) <= (1 == gcd(x, 7)) or (x + a >= 25)


for a in range(1, 1000):
    if all([f(x, a) for x in range(1, 10000)]):
        print(a)
