clastera = [[], []]

for line in open('18056a'):
    x, y = list(map(float, line.split()))
    if x < -1 and y < -2 or x > 2 and y > 1:
        pass
    elif y > x - 1:
        clastera[0].append([x, y])
    else:
        clastera[1].append([x, y])

clasterb = [[], [], []]

for line in open('18056b'):
    x, y = list(map(float, line.split()))
    if x < 0 and y < -3 or x < -2 and y > 5 or x > 4:
        pass
    elif y < 0 and y < x - 1:
        clasterb[0].append([x, y])
    elif y < -x + 3:
        clasterb[1].append([x, y])
    else:
        clasterb[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centera = [center(x) for x in clastera]

px = sum([x for x, y in centera]) / 2 * 100_000
py = sum([y for x, y in centera]) / 2 * 100_000

print(int(px), int(py))

centerb = [center(x) for x in clasterb]

px = sum([x for x, y in centerb]) / 3 * 100_000
py = sum([y for x, y in centerb]) / 3 * 100_000

print(int(px), int(py))