from fnmatch import fnmatch


def divs(n):
    sm = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sm += i
            if n // i != i:
                sm += (n // i)
    return sm


z = 0
for i in range(10 ** 10):
    if i % 6 == 0 and i % 7 == 0 and i % 8 == 0:
        if fnmatch(str(i), '?6*6*?6'):
            print(i, divs(i))
            z += 1
    if z == 7:
        break