data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    arr = sorted(line)
    if arr[-1] < sum(arr[:-1]):
        if len(set(line)) == 3:
            k += 1
print(k)