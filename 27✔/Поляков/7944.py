# data = [list(map(float, line.split()))[1] for line in open('7944b')]
#
# with open('111', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')


clasterA = [[], []]

for line in open('7944a'):
    x, y = list(map(float, line.split()))
    if x > 1.2:
        clasterA[0].append([x, y])
    else:
        clasterA[1].append([x, y])

print(len(clasterA[0]), len(clasterA[1]))
clasterB = [[], [], []]

for line in open('7944b'):
    x, y = list(map(float, line.split()))
    if x > 5:
        clasterB[0].append([x, y])
    elif y > 6:
        clasterB[1].append([x, y])
    else:
        clasterB[2].append([x, y])

print(len(clasterB[0]), len(clasterB[1]), len(clasterB[2]))

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(k):
    m = []
    for p in k:
        sm = sum([dist(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


centA = [center(x) for x in clasterA]

px = sum([x for x, y in centA]) / 2 * 10000
py = sum([y for x, y in centA]) / 2 * 10000

print(int(px), int(py))

centB = [center(x) for x in clasterB]

px = sum([x for x, y in centB]) / 3 * 10000
py = sum([y for x, y in centB]) / 3 * 10000

print(int(px), int(py))