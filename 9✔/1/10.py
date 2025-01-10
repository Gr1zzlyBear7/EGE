data = [list(map(int, line.split())) for line in open('10')]

k = 0
total = 0
for line in data:
    new = sorted(line)
    if sum(line) == 180:
        total += 1
        if line[0] == line[1] == line[2]:
            k += 1
        elif new[1] == new[0] or new[1] == new[2] or new[2] == new[0]:
            k += 1

print(k / total * 100)