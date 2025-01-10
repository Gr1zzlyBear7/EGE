data = [list(map(int, line.split())) for line in open('18')]
k = 0
for line in data:
    if line.count(min(line)) == 1:
        arr = [x for x in line if line.count(x) > 1]
        if arr:
            if max(line) + min(line) < sum(arr):
                k += 1
                print(arr)

print(k)