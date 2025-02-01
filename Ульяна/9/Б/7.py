data = [list(map(int, x.split())) for x in open('7')]
k = 0
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if c1.count(2) == 3 and len(c1) == 4:
        arr = sorted(line, key=lambda x: (line.count(x), x))
        sr = (arr[1] + arr[-1]) / 2
        if arr[0] > sr:
            k += 1
print(k)