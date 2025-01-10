data = [list(map(int, l.split())) for l in open('11')]
k = 0
for line in data:
    new = sorted(line)
    if sum(new) == 180:
        if new[-1] > 90:
            k += 1

print(k)