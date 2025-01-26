clasterA = [[], [], []]
for z in open('27a'):
    x, y = list(map(float, z.split()))
    if x < 5:
        clasterA[0].append([x, y])
    elif y > 4.9:
        clasterA[1].append([x, y])
    else:
        clasterA[2].append([x, y])

clasterB = [[], [], [], [], []]
for z in open('27b'):
    x, y = list(map(float, z.split()))
    if x < 10:
        if y > x:
            clasterB[0].append([x, y])
        else:
            clasterB[1].append([x, y])
    elif y < 10:
        clasterB[2].append([x, y])
    else:
        if y > x:
            clasterB[3].append([x, y])
        else:
            clasterB[4].append([x, y])


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
px = abs(sum([x for x, y in centerA])) / 3 * 100_000
py = abs(sum([y for x, y in centerA])) / 3 * 100_000
print(int(px), int(py))

centerB = [center(x) for x in clasterB]
px = abs(sum([x for x, y in centerB])) / 5 * 100_000
py = abs(sum([y for x, y in centerB])) / 5 * 100_000
print(int(px), int(py))