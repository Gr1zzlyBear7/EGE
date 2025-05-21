clA = [[], []]
for z in open('27a.txt'):
    x, y = list(map(float, z.split()))
    if x < 8:
        clA[0].append([x, y])
    else:
        clA[1].append([x, y])


clB = [[], [], []]
for z in open('27b.txt'):
    x, y = list(map(float, z.split()))
    if x < -0.4:
        clB[0].append([x, y])
    elif y < 4.8:
        clB[1].append([x, y])
    else:
        clB[2].append([x, y])


def dist1(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def dist2(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return abs(x2 - x1) + abs(y2 - y1)


def center1(k):
    m = []
    for p in k:
        sm = sum([dist1(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


def center2(k):
    m = []
    for p in k:
        sm = sum([dist2(p, p1) for p1 in k])
        m.append([sm, p])
    return min(m)[1]


# centerA1 = [center1(x) for x in clA]
# centerA2 = [center2(x) for x in clA]
# print(centerA1)
# print(centerA2)

# print(dist1([4.954530954767877, -2.344738834530588], [4.954530954767877, -2.344738834530588]))
# print(dist1([10.246840343877835, -1.3190662843964578], [10.246840343877835, -1.3190662843964578]))

# centerB1 = [center1(x) for x in clB]
# centerB2 = [center2(x) for x in clB]
# print(centerB1)
# print(centerB2)

print(dist1([-1.9021156698876553, 2.813280659187998], [-1.9021156698876553, 2.813280659187998]))
print(dist1([1.2479509977925116, 3.274242878766365], [1.2479509977925116, 3.274242878766365]))
print(dist1([1.3987444221215486, 5.98683652386787], [1.3626851848106751, 5.95188295918579]) * 10000)