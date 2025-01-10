data = [list(map(int, line.split())) for line in open('13')]

k = 0
for line in data:
    if line[0] + line[1] + line[2] > line[3] and \
            line[1] + line[2] + line[3] > line[0] and \
            line[3] + line[0] + line[2] > line[1] and \
            line[3] + line[1] + line[0] > line[2]:
            k += 1
print(k)