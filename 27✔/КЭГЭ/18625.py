# data = [list(map(float, line.split()))[1] for line in open('18625b')]
#
#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')

ckastersA = [[], []]

for line in open('18625a'):
    x, y = list(map(float, line.split()))
    if y < 1 or x > 10 and y < 2:
        pass
    elif x < 7 and y < 5 or x < 3:
        ckastersA[0].append([x, y])
    else:
        ckastersA[1].append([x, y])

ckastersB = [[], [], []]

for line in open('18625b'):
    x, y = list(map(float, line.split()))
    if x < 2 and y > 8 or x > 6 and y < -1 or x > 10 and y < 4:
        pass
    elif x < 7 and y < 2 or x < 2 and y < 5:
        ckastersB[0].append([x, y])
    elif y > -2/5 * x + 8 or y > x * 0.5 + 4:
        ckastersB[1].append([x, y])
    else:
        ckastersB[2].append([x, y])

print(len(ckastersB[0]), len(ckastersB[1]), len(ckastersB[2]))
def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centera = [center(k) for k in ckastersA]

px = sum([x for x, y in centera]) / 2 * 100_000
py = sum([y for x, y in centera]) / 2 * 100_000

print(int(px), int(py))

centerb = [center(k) for k in ckastersB]

px = sum([x for x, y in centerb]) / 3 * 100_000
py = sum([y for x, y in centerb]) / 3 * 100_000

print(int(px), int(py))