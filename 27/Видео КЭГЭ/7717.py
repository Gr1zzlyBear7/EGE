# data = [list(map(float, line.split()))[1] for line in open('7717b')]
#
#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')


clasterA = [[], []]

for line in open('7717a'):
    x, y = list(map(float, line.split()))
    if x < 4 and y > 0:
        clasterA[0].append([x, y])
    elif x > 4 and y < 5:
        clasterA[1].append([x, y])

clasterB = [[], [], []]

for line in open('7717b'):
    x, y = list(map(float, line.split()))
    if (x < -5 and y > 5) or (-1 < x < 1 and y < -2) or (x > 3 and y > 9):
        pass
    elif x < 0 and y < -x + 1:
        clasterB[0].append([x, y])
    elif y > -x + 1 and y > 0.5 * x + 3:
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

pxa = sum([x for x, y in centerA]) / 2 * 100_000
pya = sum([y for x, y in centerA]) / 2 * 100_000

print(int(pxa), int(pya))

centerB = [center(x) for x in clasterB]

pxb = sum([x for x, y in centerB]) / 3 * 100_000
pyb = sum([y for x, y in centerB]) / 3 * 100_000

print(int(pxb), int(pyb))