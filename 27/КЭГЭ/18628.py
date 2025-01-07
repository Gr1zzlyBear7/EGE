# data = [list(map(float, line.split()))[1] for line in open('18628b').readlines()]
#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')


clastersA = [[], []]

for line in open('18628a'):
    x, y = list(map(float, line.split()))
    if y > x + 3:
        clastersA[0].append([x, y])
    else:
        clastersA[1].append([x, y])

clastersb = [[], [], []]

for line in open('18628b'):
    x, y = list(map(float, line.split()))
    if y < -x + 2:
        clastersb[0].append([x, y])
    elif y > 5/3 * x + 3:
        clastersb[1].append([x, y])
    else:
        clastersb[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(x) for x in clastersA]

px = sum([x for x, y in centerA]) / 2 * 100_000
py = sum([y for x, y in centerA]) / 2 * 100_000

print(int(px), int(py))

centerB = [center(x) for x in clastersb]

px = sum([x for x, y in centerB]) / 3 * 100_000
py = sum([y for x, y in centerB]) / 3 * 100_000

print(int(px), int(py))