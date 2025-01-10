data = [list(map(int, line.split())) for line in open('19')]

k = 0
for line in data:
    if 0 in (line[0], line[1]) and 0 in (line[2], line[3]):
        k += 1

print(k)