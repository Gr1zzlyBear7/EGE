from fnmatch import fnmatch


def div(n):
    sm = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2:
                sm += i
            if n // i != i:
                if (n // i) % 2:
                    sm += n // i
    return sm


z = 0
for n in range(10 ** 7, -1, -1):
    if n % 217 == 0:
        if fnmatch(str(n), '14?4*'):
            print(n, div(n))
            z += 1
    if z == 7:
        break