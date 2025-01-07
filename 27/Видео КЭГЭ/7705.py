# data = [list(map(float, line.split()))[1] for line in open('7705b')]
#
#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')

clasterA = [[], []]

for line in open('7705a'):
    x, y = list(map(float, line.split()))
    if x > 2 and y < 4:
        clasterA[0].append([x, y])
    elif y > -3 and x < 5:
        clasterA[1].append([x, y])

clasterB = [[], [], []]

for line in open('7705b'):
    x, y = list(map(float, line.split()))
    if (x < 0 and y < 2) or (x < 2 and y < -2) or (x > 6 and y > 8):
        pass
    elif (x < 5 and y > 7) or (x < 3 and y > 0):
        clasterB[0].append([x, y])
    elif (y < 0) or (x > 5 and y <= 3) or (x > 7 and y < 5):
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


centera = [center(k) for k in clasterA]

pxa = sum([x for x, y in centera]) / 2 * 100000
pya = sum([y for x, y in centera]) / 2 * 100000

print(int(pxa), int(pya))

centerb = [center(k) for k in clasterB]

pxb = sum([x for x, y in centerb]) / 3 * 100000
pyb = sum([y for x, y in centerb]) / 3 * 100000

print(int(pxb), int(pyb))
