data = [list(map(int, line.split())) for line in open('9')]

k = 0
for line in data:
    arr = [line.count(x) for x in set(line)]
    if 3 in arr and len(arr) == 4:
        new = sorted(line, key=line.count)
        rep = new[3:]
        one = new[:3]
        if sum(rep) ** 2 > sum(one) ** 2:
            k += 1

print(k)