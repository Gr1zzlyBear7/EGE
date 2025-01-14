# data = [list(map(float, line.split()))[1] for line in open('7709b')]

#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')

clasA = [[], []]

for line in open('7709a'):
    x, y = list(map(float, line.split()))
    if y < -x + 13:
        clasA[0].append([x, y])
    else:
        clasA[1].append([x, y])

clasB = [[], [], []]

for line in open('7709b'):
    x, y = list(map(float, line.split()))
    if y < 2:
        clasB[0].append([x, y])
    elif y < -7/5 * x + 16.8:
        clasB[1].append([x, y])
    else:
        clasB[2].append([x, y])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def center(k):
    m = []
    for p in k:
        sm = sum(dist(p, p1) for p1 in k)
        m.append([sm, p])
    return min(m)[1]


centera = [center(k) for k in clasA]
centerb = [center(k) for k in clasB]

pxa = sum([x for x, y in centera]) / 2 * 100000
pya = sum([y for x, y in centera]) / 2 * 100000

print(pxa, pya)

pxb = sum([x for x, y in centerb]) / 3 * 100000
pyb = sum([y for x, y in centerb]) / 3 * 100000

print(pxb, pyb)