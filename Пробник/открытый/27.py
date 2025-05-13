clA = [[], []]
for z in open('27a.txt'):
    x, y = list(map(float, z.split()))
    if y > 2:
        clA[0].append([x, y])
    else:
        clA[1].append([x, y])

clb = [[], [], []]
for z in open('27b.txt'):
    x, y = list(map(float, z.split()))
    if x < 10:
        clb[0].append([x, y])
    elif x < 20:
        clb[1].append([x, y])
    else:
        clb[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = [dist(p, p1) for p1 in k]
        m.append([sm, p])
    return min(m)[1]


cA = [center(x) for x in clA]
px = sum([x for x, y in cA]) / 2 * 10000
py = sum([y for x, y in cA]) / 2 * 10000
print(int(px), int(py))

cB = [center(x) for x in clb]
px = sum([x for x, y in cB]) / 3 * 10000
py = sum([y for x, y in cB]) / 3 * 10000
print(int(px), int(py))
