data = [list(map(int, line.split())) for line in open('8')]
k = 0
for line in data:
    new = sorted(line)
    if new[-1] - new[0] >= 50:
        if new[1] * new[2] <= 1000:
            k += 1

print(k)