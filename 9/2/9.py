data = [list(map(int, line.split())) for line in open('9')]
k = 0
for line in data:
    new = sorted(line)
    if new[-1] ** 3 >= new[0] * new[1] * new[2] * 2:
        if len([x for x in new if x > 10]) == 4:
            k += 1

print(k)