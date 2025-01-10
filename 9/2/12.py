data = [list(map(int, line.split())) for line in open('12')]
k = 0
for line in data:
    new = sorted(line)
    arr = [line.count(x) for x in set(line)]
    if (new[0] + new[-1]) ** 2 > new[1] ** 2 + new[2] ** 2 + new[3] ** 2 + new[4] ** 2:
        k += 1
    elif arr.count(3) == 1 and len(arr) == 4:
        k += 1

print(k)