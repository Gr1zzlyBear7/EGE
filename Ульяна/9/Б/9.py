data = [list(map(int, x.split())) for x in open('9')]
k = 0
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if 2 in c1 and len(c1) == 6:
        arr = sorted(line, key=lambda x: (line.count(x), x))
        if arr[0] * arr[1] * arr[2] > arr[-1] ** 2:
            k += 1
print(k)