data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    arr = sorted(line)
    ma_mi = [arr.pop(0), arr.pop()]
    if sum(ma_mi) ** 2 > arr[0] ** 2 + arr[1] ** 2 + arr[2] ** 2:
        k += 1
print(k)