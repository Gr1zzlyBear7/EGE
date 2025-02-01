data = [list(map(int, x.split())) for x in open('8')]
k = 1
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if 2 in c1 and len(c1) == 5:
        arr = sorted(line, key=line.count)
        if sum(arr[:4]) / 4 <= arr[-1]:
            print(k)
            break
    k += 1