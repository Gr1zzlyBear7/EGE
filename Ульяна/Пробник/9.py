data = [list(map(int, x.split())) for x in open('9var1.txt')]
k = 0
for line in data:
    if len(set(line)) == len(line):
        if max(line) < sum(line) - max(line):
            k += 1
print(k)