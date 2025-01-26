clasterA = [[], []]
for line in open('27a'):
    x, y = list(map(float, line.split()))
    if x > 23.5:
        clasterA[0].append([x, y])
    else:
        clasterA[1].append([x, y])

clasterB = [[], [], []]
for line in open('27b'):
    x, y = list(map(float, line.split()))
    if x < -14:
        clasterB[0].append([x, y])
    elif x < 15:
        clasterB[1].append([x, y])
    else:
        clasterB[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return abs(x2 - x1) + abs(y2 - y1)


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(x) for x in clasterA]
px = sum([x for x, y in centerA]) / 2 * 1000
py = sum([y for x, y in centerA]) / 2 * 1000
print(int(px), int(py))
centerB = [center(x) for x in clasterB]
px = sum([x for x, y in centerB]) / 3 * 1000
py = sum([y for x, y in centerB]) / 3 * 1000
print(int(px), int(py))