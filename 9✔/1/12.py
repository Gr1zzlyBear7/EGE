data = [list(map(int, line.split())) for line in open('12')]

k = 0
for line in data:
    if sum(line) == 360:
        if line[0] == line[2] and line[3] == line[1]:
            k += 1

print(k)