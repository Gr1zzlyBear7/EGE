data = [list(map(int, x.split())) for x in open('6')]
k = 0
for line in data:
    c1 = [line.count(x) for x in set(line)]
    if 3 in c1 and len(c1) == 5:
        arr = sorted(line, key=line.count)
        povt = [arr.pop(), arr.pop(), arr.pop()]
        if sum(arr) / len(arr) <= povt[0]:
            k += 1
print(k)