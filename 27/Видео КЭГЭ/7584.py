clustersa = [[], []]

for line in open('7584a'):
    x, y = list(map(float, line.split()))
    if x > 3:
        clustersa[1].append([x, y])
    else:
        clustersa[0].append([x, y])

clastersb = [[], [], []]

for line in open('7584b'):
    x, y = list(map(float, line.split()))
    if x > 4:
        clastersb[0].append([x, y])
    elif y > 2.3:
        clastersb[1].append([x, y])
    else:
        clastersb[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum(dist(p, p1) for p1 in k)
        m.append([sm, p])
    return min(m)[1]


centera = [center(k) for k in clustersa]
centerb = [center(k) for k in clastersb]


pxa = sum(x for x, y in centera) / 2 * 10000
pya = sum(y for x, y in centera) / 2 * 10000

pxb = sum(x for x, y in centerb) / 3 * 10000
pyb = sum(y for x, y in centerb) / 3 * 10000

print(pxa, pya)
print(pxb, pyb)