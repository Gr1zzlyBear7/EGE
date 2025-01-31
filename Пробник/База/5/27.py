clasterA = [[], []]
for z in open('27a.txt'):
    x, y = map(float, z.split())
    if x < 1 and y < 0:
        pass
    elif x < 13 and y > 13.3:
        pass
    elif 14 < x < 16 and y < 5:
        pass
    elif x > 27 and y > 15.5:
        pass
    elif x < 13:
        clasterA[0].append([x, y])
    else:
        clasterA[1].append([x, y])

clasterB = [[], [], [], []]
for z in open('27b.txt'):
    x, y = map(float, z.split())
    if x < -90 and -20 > y > -30:
        pass
    elif -20 < x < 0 and -10 > y > -30:
        pass
    elif -20 < x < 0 and 70 < y < 90:
        pass
    elif 90 < x < 110 and 10 > y > 0:
        pass
    elif x < 0:
        if y > -20:
            clasterB[0].append([x, y])
        else:
            clasterB[1].append([x, y])
    else:
        if y > -10:
            clasterB[2].append([x, y])
        else:
            clasterB[3].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centerA = [center(x) for x in clasterA]
px = sum([x for x, y in centerA]) / 2 * 10_000
py = sum([y for x, y in centerA]) / 2 * 10_000
print(int(px), int(py))

centerB = [center(x) for x in clasterB]
px = sum([x for x, y in centerB]) / 4 * 10_000
py = sum([y for x, y in centerB]) / 4 * 10_000
print(int(px), int(py))