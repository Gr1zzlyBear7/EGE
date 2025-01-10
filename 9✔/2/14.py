data = [list(map(int, line.split())) for line in open('14')]
k = 1
for line in data:
    arr = [line.count(x) for x in set(line)]
    if len(arr) == 5 and 2 in arr:
        new = sorted(line, key=line.count)
        if sum(new[0:4]) / 4 <= new[-1]:
            print(k)
            break
    k += 1
