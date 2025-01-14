# data = [list(map(float, line.split()))[1] for line in open('18676b').readlines()]
#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')


clastersA = [[], []]

for line in open('18676a'):
    x, y = list(map(float, line.split()))
    if x < 6 and y > -1 and y > x - 5:
        clastersA[0].append([x, y])
    else:
        clastersA[1].append([x, y])

clastersB = [[], [], []]

for line in open('18676b'):
    x, y = list(map(float, line.split()))
    if x < 9 and y > 5 or x < 4 and y > 0:
        clastersB[0].append([x, y])
    elif x < 9 and y > 0 and y > x - 6:
        clastersB[1].append([x, y])
    else:
        clastersB[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centera = [center(x) for x in clastersA]

px = sum([x for x, y in centera]) / 2 * 100_000
py = sum([y for x, y in centera]) / 2 * 100_000

print(int(px), int(py))

centerb = [center(x) for x in clastersB]

px = sum([x for x, y in centerb]) / 3 * 100_000
py = sum([y for x, y in centerb]) / 3 * 100_000

print(int(px), int(py))
