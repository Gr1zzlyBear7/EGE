data = [list(map(int, line.split())) for line in open('11')]
k = 0
for line in data:
    arr = [line.count(x) for x in set(line)]
    if len(arr) == 4 and arr.count(3) == 1:
        new = (sorted(line, key=line.count))
        same = new[3:]
        not_same = new[:3]
        if sum(not_same) / 3 <= sum(same):
            k += 1

print(k)