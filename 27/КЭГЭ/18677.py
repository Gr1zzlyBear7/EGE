# data = [list(map(float, line.split()))[1] for line in open('18677b')]
#
#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')


clastesA = [[], []]

for line in open('18677a'):
    x, y = list(map(float, line.split()))
    if x < 3 and y > 1.5 or x > 7 and y < -1:
        pass
    elif y > 4 / 3 * x - 16 / 3:
        clastesA[0].append([x, y])
    else:
        clastesA[1].append([x, y])

clastesB = [[], [], []]

for line in open('18677b'):
    x, y = list(map(float, line.split()))
    if x < 5 and y > 7 or x > 10 and y > 9 or x > 9 and y < -2:
        pass
    elif x < 8 and y < 1.5 or x < 4.6 and y < 7:
        clastesB[0].append([x, y])
    elif x < 8 and y < 7 and y < -x + 14:
        clastesB[1].append([x, y])
    else:
        clastesB[2].append([x, y])


print(len(clastesB[0]), len(clastesB[1]), len(clastesB[2]))
def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 -x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centera = [center(x) for x in clastesA]

px = sum([x for x, y in centera]) / 2 * 100_000
py = sum([y for x, y in centera]) / 2 * 100_000

print(int(px), int(py))

centerb = [center(x) for x in clastesB]

px = sum([x for x, y in centerb]) / 3 * 100_000
py = sum([y for x, y in centerb]) / 3 * 100_000

print(int(px), int(py))