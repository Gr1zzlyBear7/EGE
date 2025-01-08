data = [list(map(int, line.split('\t'))) for line in open('9').readlines()]

k = 0
ans = []

for line in data:
    arr = [line.count(x) for x in set(line)]
    if 3 in arr and len(set(line)) == 4:
        new = sorted(line, key=line.count)
        rep = new.pop(3), new.pop(3), new.pop(3)
        if sum(new) ** 2 < sum(rep) ** 2:
            k += 1
            print(new, rep)
print(k)