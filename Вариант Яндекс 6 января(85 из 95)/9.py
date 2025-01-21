data = [list(map(float, line.split())) for line in open('9')]
ans = []
k = 0
for line in data:
    if line[1] <= line[0] - 5:
        if 0 <= line[2] <= 45 or 315 <= line[2] <= 360:
            k += 1
print(k)