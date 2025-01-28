data = [list(map(int, x.split())) for x in open('9')]
k = 0
for line in data:
    if len(set(line)) == len(line):
        new = sorted(line)
        arr = [new.pop(0), new.pop()]
        if sum(arr) * 2 <= sum(new) * 3:
            k += 1
print(k)