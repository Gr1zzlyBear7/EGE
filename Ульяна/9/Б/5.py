data = [list(map(int, x.split())) for x in open('5')]
k = 0
for line in data:
    if len(set(line)) == len(line):
        arr = sorted(line)
        ma_mi = [arr.pop(0), arr.pop()]
        if sum(ma_mi) * 3 >= sum(arr) * 2:
            k += 1
print(k)