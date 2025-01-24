def f(x, a):
    q = [y for y in range(29, 48)]
    p = [48, 52, 56]
    return ((x % 3 != 0) and (x not in p)) <= ((abs(x - 50) <= 7) <= (x in q)) or (x & a == 0)


for a in range(0, 100):
    if all([f(x, a) for x in range(1, 1000)]):
        print(a)

