data = [list(map(int, line.split())) for line in open('7')]
k = 0
for line in data:
    new = sorted(line)
    if new[-1] * new[0] == new[1] * new[2]:
        print(new)
        if new[-2] ** 2 > new[0] * new[-1]:
            k += 1

print(k)