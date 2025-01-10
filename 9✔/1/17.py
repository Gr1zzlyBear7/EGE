data = [list(map(int, line.split())) for line in open('17')]
k = 0
for line in data:
    if line[0] > 0 and line[2] > 0 and line[1] > 0 and line[3] > 0 or \
            line[0] < 0 and line[2] < 0 and line[1] > 0 and line[3] > 0 or \
            line[0] < 0 and line[2] < 0 and line[1] < 0 and line[3] < 0 or \
            line[0] > 0 and line[2] > 0 and line[1] < 0 and line[3] < 0:
        k += 1

print(k)
