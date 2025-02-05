clA = [[], []]
for z in open('27a.txt'):
    x, y, h = map(float, z.split())
    if x < 200:
        clA[0].append([x, y, h])
    elif x > 320:
        clA[1].append([x, y, h])
clB = [[], [], []]
for z in open('27b.txt'):
    x, y, h = map(float, z.split())
    if x < 0 and y < 0:
        clB[0].append([x, y, h])
    elif -150 <= x <= 50 and y > -25:
        clB[1].append([x, y, h])
    elif 70 <= x <= 225:
        clB[2].append([x, y, h])


def dist(p1, p2):
    x1, y1, h1, x2, y2, h2 = *p1, *p2
    return (((x2 - x1) ** 2 + (y1 - y2) ** 2) ** 0.5) * h2


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(x) for x in clA]
px = sum([x for x, y, h in centerA]) / 2 * 100_000
py = sum([y for x, y, h in centerA]) / 2 * 100_000
print(int(px), int(py))
centerB = [center(x) for x in clB]
px = sum([x for x, y, h in centerB]) / 3 * 100_000
py = sum([y for x, y, h in centerB]) / 3 * 100_000
print(int(px), int(py))

