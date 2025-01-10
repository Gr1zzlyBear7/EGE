data = [list(map(int, line.split())) for line in open('1')]

k = 0
for line in data:
    new = sorted(line)
    if (new[0] + new[2]) / 2 <= new[1]:
        k += 1

print(k)