data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    if max(line) < sum(line) - max(line):
        arr = [line.count(x) for x in set(line)]
        if len(arr) == 3 and 2 in arr:
            k += 1
        # if len(set(line)) == 3:
        #     k += 1
print(k)