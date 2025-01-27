clasterA = [[], [], []]
for z in open('27a'):
    x, y = list(map(float, z.split()))
    if x < 6:
        clasterA[0].append([x, y])
    elif y > 23:
        clasterA[1].append([x, y])
    else:
        clasterA[2].append([x, y])


clasterB = [[], [], [], []]
for z in open('27b'):
    x, y = list(map(float, z.split()))
    if x < 15.4:
        if y < 15:
            clasterB[0].append([x, y])
        else:
            clasterB[1].append([x, y])
    elif y > 15:
        clasterB[2].append([x, y])
    else:
        clasterB[3].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(x) for x in clasterA]
px = sum([x for x, y in centerA]) / 3 * 10000
py = sum([y for x, y in centerA]) / 3 * 10000
print(int(px), int(py))

centerB = [center(x) for x in clasterB]
px = sum([x for x, y in centerB]) / 4 * 10000
py = sum([y for x, y in centerB]) / 4 * 10000
print(int(px), int(py))