clA = [[], []]
for z in open('27a.txt'):
    x, y = map(float, z.split())
    if x < 0:
        clA[0].append([x, y])
    else:
        clA[1].append([x, y])

clB = [[], [], []]
for z in open('27b.txt'):
    x, y = map(float, z.split())
    if x < 0:
        clB[0].append([x, y])
    elif x < 6:
        clB[1].append([x, y])
    else:
        clB[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(x) for x in clA]
px = sum([x for x, y in centerA]) / 2 * 1000
py = sum([y for x, y in centerA]) / 2 * 1000
print(int(px), int(py))
centerB = [center(x) for x in clB]
px = sum([x for x, y in centerB]) / 3 * 1000
py = sum([y for x, y in centerB]) / 3 * 1000
print(int(px), int(py))