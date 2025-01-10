data = [list(map(int, line.split())) for line in open('5')]

k = 0
for line in data:
    if (line[0] + line[1]) / 2 == line[2] or \
            (line[1] + line[2]) / 2 == line[0] or\
            (line[0] + line[2]) / 2 == line[1]:
            k += 1
print(k)