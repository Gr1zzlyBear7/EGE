clasterA = [[], [], []]
for z in open('27a.txt'):
    x, y = map(float, z.split())
    if x < 0:
        clasterA[0].append([x, y])
    elif x < 3:
        clasterA[1].append([x, y])
    else:
        clasterA[2].append([x, y])
clasterA = [clasterA[0], clasterA[2]]

clasterB = [[], [], [], [], []]
for z in open('27b.txt'):
    x, y = map(float, z.split())
    if x < -1:
        clasterB[0].append([x, y])
    elif x < 1.8 and y < 4.3:
        clasterB[1].append([x, y])
    elif y < 5.3:
        clasterB[2].append([x, y])
    elif x < 3:
        clasterB[3].append([x, y])
    else:
        clasterB[4].append([x, y])
new_clasterB = clasterB[:3]
new_clasterB.append(clasterB[4])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        r = max([dist(p, p1) for p1 in k])
        m.append([sm, r, p])
    return min(m)


centerA = [center(x) for x in clasterA]
r1 = (centerA[0][1] + centerA[1][1]) / 2
print(int(r1 * 10000))
centerB = [center(x) for x in new_clasterB]
r1 = (centerB[0][1] + centerB[1][1] + centerB[2][1] + centerB[3][1]) / 4
print(int(r1 * 10000))
