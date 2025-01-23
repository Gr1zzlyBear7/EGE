from fnmatch import fnmatch


def divs(n):
    k = 0
    sm = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                k += 1
                sm += i
            if n // i != i:
                if (n // i) % 2 == 0:
                    k += 1
                    sm += n // i
    return k >= 4, sm


z = 0
for n in range(65000, 100000000):
    if divs(n)[0]:
        if fnmatch(str(n), '6*97*5?'):
            print(n, divs(n)[1])
            z += 1
    if z == 7:
        break