data = [list(map(int, x.split())) for x in open('3')]
k = 0
for line in data:
    arr = sorted(line)
    ma_mi = [arr.pop(0), arr.pop()]
    if sum(ma_mi) < sum(arr):
        k += 1
print(k)