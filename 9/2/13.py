data = [list(map(int, line.split())) for line in open('13')]
k = 0
for line in data:
    arr = [line.count(x) for x in set(line)]
    if len(arr) == 5 and 3 in arr:
        new = sorted(line, key=line.count)
        if sum(new[0:4]) / 4 <= new[-1]:
            k += 1

print(k)