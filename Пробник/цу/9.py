data = [list(map(int, x.split())) for x in open('9.txt')]

k = 0
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if c1.count(2) == 2 and len(set(line)) == 5:
        arr = sorted(line, key=line.count)
        sub1 = arr[0:3]
        sub2 = arr[3:]
        if sum(sub1) / 3 <= sum(line) / 7:
            k += 1
print(k)