def f(x, a):
    return (x % a == 0) or ((x % 133 == 0) <= (x % 95 != 0))


for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 100000)):
        print(a)