clA = [[], []]
for z in open('A'):
    x, y = list(map(float, z.split()))
    if y < 2.5:
        clA[0].append([x, y])
    elif 1 < x < 6:
        clA[1].append([x, y])

print(len(clA[0]), len(clA[1]))
clB = [[], [], []]
for z in open('B'):
    x, y = list(map(float, z.split()))
    if y > 9 and x < 4 or y > 9 and x > 8 or y < -1.5:
        pass
    elif x < 3 or y < -1.5 * x + 7.5:
        clB[0].append([x, y])
    elif y > -1 * x + 13 or y < 6 * x - 36:
        clB[1].append([x, y])
    else:
        clB[2].append([x, y])

print(len(clB[0]), len(clB[1]), len(clB[2]))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(x) for x in clA]
px = sum([x for x, y in centerA]) / 2 * 100_000
py = sum([y for x, y in centerA]) / 2 * 100_000
print(int(px), int(py))

centerB = [center(x) for x in clB]
px = sum([x for x, y in centerB]) / 3 * 100_000
py = sum([y for x, y in centerB]) / 3 * 100_000
print(int(px), int(py))