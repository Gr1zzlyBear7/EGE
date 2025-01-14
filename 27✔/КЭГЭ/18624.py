# data = [list(map(float, line.split()))[1] for line in open('18624b').readlines()]
#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')


clasterA = [[], []]

for line in open('18624a'):
    x, y = list(map(float, line.split()))
    if x > 4 and y > 4:
        clasterA[0].append([x, y])
    elif x > 6 and y < 4:
        clasterA[0].append([x, y])
    else:
        clasterA[1].append([x, y])


clasterB = [[], [], []]

for line in open('18624b'):
    x, y = list(map(float, line.split()))
    if x < 4 and y < 2 or x < 1 and y > 2:
        clasterB[0].append([x, y])
    elif x < 7 and y < 5 or x < 4 and y < 5:
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

px = sum([x for x, y in centerA]) / 2 * 100_000
py = sum([y for x, y in centerA]) / 2 * 100_000

print(int(px), int(py))

centerB = [center(x) for x in clasterB]

px = sum([x for x, y in centerB]) / 3 * 100_000
py = sum([y for x, y in centerB]) / 3 * 100_000

print(int(px), int(py))