clasterA = [[], [], [], []]
for z in open('27a.txt'):
    x, y = map(float, z.split())
    if x < 10.5:
        if y < 14:
            clasterA[0].append([x, y])
        else:
            clasterA[1].append([x, y])
    else:
        if y > 8:
            clasterA[2].append([x, y])
        else:
            clasterA[3].append([x, y])
clasterB = [[], [], [], [], []]
for z in open('27b.txt'):
    x, y = map(float, z.split())
    if x < 13:
        if y > 10:
            clasterB[0].append([x, y])
        else:
            clasterB[1].append([x, y])
    elif x < 28:
        if y > 4.5:
            clasterB[2].append([x, y])
        else:
            clasterB[3].append([x, y])
    else:
        clasterB[4].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(x) for x in clasterA]
px = sum([x for x, y in centerA]) / 4 * 10_000
py = sum([y for x, y in centerA]) / 4 * 10_000
print(int(px), int(py))
centerB = [center(x) for x in clasterB]
px = sum([x for x, y in centerB]) / 5 * 10_000
py = sum([y for x, y in centerB]) / 5 * 10_000
print(int(px), int(py))