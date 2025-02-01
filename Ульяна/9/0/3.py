data = [list(map(int, x.split())) for x in open('3')]
k = 0
for line in data:
    if max(line) < sum(line) - max(line):
        c2 = [line.count(x) for x in set(line)]
        if len(c2) == 3 and 2 in c2:
            k += 1
print(k)