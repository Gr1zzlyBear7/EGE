data = [list(map(int, x.split())) for x in open('4')]
k = 1
z = 0
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if 3 in c1 and 2 in c1 and len(c1) == 5:
        arr = sorted(line, key=line.count)
        if arr[4] < arr[-1]:
            z += 1
    if z == 3:
        print(k)
        break
    k += 1