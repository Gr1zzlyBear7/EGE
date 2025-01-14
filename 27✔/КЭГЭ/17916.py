clastersA = [[], []]

for line in open('17916a'):
    x, y = list(map(float, line.split()))
    if y > 8:
        clastersA[0].append([x, y])
    else:
        clastersA[1].append([x, y])

clastersB = [[], [], [], [], []]

for line in open('17916b'):
    x, y = list(map(float, line.split()))
    if x > 12:
        clastersB[0].append([x, y])
    elif y < 5.5:
        clastersB[1].append([x, y])
    elif y < 9:
        clastersB[2].append([x, y])
    elif y < 13:
        clastersB[3].append([x, y])
    else:
        clastersB[4].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(k) for k in clastersA]

pxa = sum([x for x, y in centerA]) / 2 * 10000
pya = sum([y for x, y in centerA]) / 2 * 10000

print(int(pxa), int(pya))

centerB = [center(k) for k in clastersB]

pxa = sum([x for x, y in centerB]) / 5 * 10000
pya = sum([y for x, y in centerB]) / 5 * 10000

print(int(pxa), int(pya))