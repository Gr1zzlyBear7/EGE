data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    if len(set(line)) == 5:
        arr = sorted(line)
        if arr[-1] + arr[-2] <= sum(arr[:3]):
            k += 1
print(k)