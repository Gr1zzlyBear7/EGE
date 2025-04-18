clA = [[], []]
for line in open('27a.txt'):
    x, y = list(map(float, line.split()))
    if y > 10:
        clA[0].append([x, y])
    else:
        clA[1].append([x, y])


clB = [[], [], []]
for line in open('27b.txt'):
    x, y = list(map(float, line.split()))
    if x < 2:
        clB[0].append([x, y])
    elif y < 5:
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
px = sum([x for x, y in centerA]) / 2 * 10000
py = sum([y for x, y in centerA]) / 2 * 10000
print(int(px), int(py))

centerB = [center(x) for x in clB]
px = sum([x for x, y in centerB]) / 3 * 10000
py = sum([y for x, y in centerB]) / 3 * 10000
print(int(px), int(py))