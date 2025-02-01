data = [list(map(int, x.split())) for x in open('6')]
k = 0
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if len(c1) == 4 and 3 in c1:
        arr = sorted(line, key=line.count)
        povt = [arr.pop(), arr.pop(), arr.pop()]
        if sum(povt) ** 2 > sum(arr) ** 2:
            k += 1
print(k)