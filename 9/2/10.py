data = [list(map(int, line.split())) for line in open('10')]
k = 0
for line in data:
    new = sorted(line)
    if new[-1] < sum(new) - max(new):
        if len(set(line)) == 3:
            k += 1

print(k)