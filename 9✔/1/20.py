data = [list(map(int, line.split())) for line in open('20')]

k = 0
for line in data:
    if ((line[0] - line[2]) ** 2 + (line[1] - line[3]) ** 2) ** 0.5 <= 5:
        if line[0] * line[2] <= 0 or 0 >= line[1] * line[3]:
            k += 1

print(k)
