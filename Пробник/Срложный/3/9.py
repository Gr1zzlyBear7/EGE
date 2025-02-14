data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    if max(line) < sum(line) - max(line):
        arr = sorted(line)
        if arr[0] + arr[-1] == arr[1] + arr[2]:
            k += 1
print(k)