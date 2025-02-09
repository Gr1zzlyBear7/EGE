data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if 3 in c1 and len(c1) == 4:
        arr = sorted(line, key=line.count)
        if sum(arr[3:]) ** 2 > sum(arr[:3]) ** 2:
            k += 1
print(k)