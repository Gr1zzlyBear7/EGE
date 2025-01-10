data = [list(map(int, line.split())) for line in open('14')]

k = 0
for line in data:
    if line[0] == line[2] and line[3] == line[1]:
        k += 1

print(k)