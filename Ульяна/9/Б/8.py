data = [list(map(int, x.split())) for x in open('8')]
k = 1
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if c1.count(3) == 2 and len(c1) == 3:
        arr = sorted(line, key=lambda x: (line.count(x), x))
        sr = sum(arr[1:]) / 6
        if sr < arr[0]:
            print(k)
    k += 1