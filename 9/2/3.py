data = [list(map(int, line.split())) for line in open('3')]
k = 0
for line in data:
    new = sorted(line)
    if new[-1] ** 2 > new[0] * new[1] * 2:
        k += 1

print(k)