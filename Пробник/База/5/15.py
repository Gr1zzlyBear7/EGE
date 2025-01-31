def f(x, a):
    return ((x % 3 == 0) <= (x % 17 != 0)) or not(a < (190 - x))


for a in range(1, 1000):
    if all([f(x, a) for x in range(1, 10000)]):
        print(a)