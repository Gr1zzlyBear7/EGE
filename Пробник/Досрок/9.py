data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    c1 = [x for x in set(line) if line.count(x) == 3]
    if len(set(line)) == 3 and len(c1) == 2:
        povt = sorted(line, key=line.count)
        np = povt[0]
        povt = povt[1:]
        if max(povt) > np:
            k += 1
print(k)
