data = [list(map(int, x.split())) for x in open('9')]
k = 0
for line in data:
    arr = [line.count(x) for x in set(line)]
    if 2 in arr and len(set(line)) == 5:
        new = sorted(line, key=line.count)
        povt = [new.pop(), new.pop()]
        sr = sum(new) / len(new)
        if sr >= sum(povt):
            k += 1
print(k)