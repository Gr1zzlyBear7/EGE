data = [list(map(int, x.split())) for x in open('9.txt')]
k = 0
for line in data:
    sr = sum(line) / len(line)
    if sr in line:
        k += 1
print(k)