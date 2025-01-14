clastersA = [[], []]

for line in open('18314a'):
    x, y = list(map(float, line.split()))
    if x > 23.5:
        clastersA[0].append([x, y])
    else:
        clastersA[1].append([x, y])

clastersB = [[], [], []]

for line in open('18314b'):
    x, y = list(map(float, line.split()))
    if x < -12:
        clastersB[0].append([x, y])
    elif x < 15:
        clastersB[1].append([x, y])
    else:
        clastersB[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return abs(x1 - x2) + abs(y1 - y2)


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(x) for x in clastersA]

px = sum([x for x, y in centerA]) / 2 * 1000
py = sum([y for x, y in centerA]) / 2 * 1000

print(int(px), int(py))

centerB = [center(x) for x in clastersB]

px = sum([x for x, y in centerB]) / 3 * 1000
py = sum([y for x, y in centerB]) / 3 * 1000

print(int(px), int(py))