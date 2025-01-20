data = [list(map(int, line.split())) for line in open('9')]
k = 0
ans = []
for line in data:
    if line[0] == line[2] and line[1] == line[3]:
        if sum(line) == 360:
            k += 1

print(k)
