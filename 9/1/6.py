data = [list(map(int, line.split())) for line in open('6')]

k = 0
for line in data:
    new = sorted(line)
    if new[1] - new[0] == new[2] - new[1] != 0:
        k += 1

print(k)