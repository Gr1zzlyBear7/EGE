clasterA = [[], []]
for line in open('27a'):
    x, y = list(map(float, line.split()))
    if y > 15:
        clasterA[0].append([x, y])
    else:
        clasterA[1].append([x, y])

clasterB = [[], [], []]
for line in open('27b'):
    x, y = list(map(float, line.split()))
    if x > 1:
        clasterB[0].append([x, y])
    elif y > 0:
        clasterB[1].append([x, y])
    else:
        clasterB[2].append([x, y])


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
px = abs(sum([x for x, y in centerA])) / 2 * 10_000
py = abs(sum([y for x, y in centerA])) / 2 * 10_000
print(int(px), int(py))
centerB = [center(x) for x in clasterB]
px = abs(sum([x for x, y in centerB])) / 3 * 10_000
py = abs(sum([y for x, y in centerB])) / 3 * 10_000
print(int(px), int(py))