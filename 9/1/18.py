data = [list(map(int, line.split())) for line in open('18')]

k = 0
for line in data:
    if line[0] * line[2] > 0 >= line[1] * line[3] or line[0] * line[2] <= 0 < line[1] * line[3]:
        k += 1

print(k)