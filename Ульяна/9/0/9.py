data = [list(map(int, x.split())) for x in open('9')]
k = 0
for line in data:
    arr = sorted(line)
    if arr[0] + arr[-1] < arr[1] + arr[2]:
        k += 1
print(k)