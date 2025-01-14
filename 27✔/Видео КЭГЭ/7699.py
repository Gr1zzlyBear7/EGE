# data = [list(map(float, line.split()))[1] for line in open('7699b')]
#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')


clusterA = [[], []]

for line in open('7699a'):
    x, y = list(map(float, line.split()))
    if y > x + 1:
        clusterA[0].append([x, y])
    else:
        clusterA[1].append([x, y])

clusterB = [[], [], []]

for line in open('7699b'):
    x, y = list(map(float, line.split()))
    if y < -x + 8:
        clusterB[0].append([x, y])
    elif y > 3 / 4 * x - 0.75:
        clusterB[1].append([x, y])
    else:
        clusterB[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum(dist(p, p1) for p1 in k)
        m.append([sm, p])
    return min(m)[1]


centera = [center(k) for k in clusterA]
centerb = [center(k) for k in clusterB]

pxa = sum(x for x, y in centera) / 2 * 100000
pya = sum(y for x, y in centera) / 2 * 100000

print(int(pxa), int(pya))

pxb = (sum(x for x, y in centerb) / 3) * 100000
pyb = (sum(y for x, y in centerb)) / 3 * 100000

print(int(pxb), int(pyb))
