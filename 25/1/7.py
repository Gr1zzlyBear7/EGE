from fnmatch import fnmatch


def divs(n):
    sm = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sm += i
            if n // i != i:
                sm += n // i
    return sm

z = 0
for i in range(10 ** 7, -1, -1):
    if fnmatch(str(i), '9?*55*7'):
        print(i, divs(i) % 21)
        z += 1
    if z == 5:
        break
