data = [list(map(int, line.split())) for line in open('16')]
k = 0
for line in data:
    if len(set(line)) == 5:
        new = sorted(line)
        if 2 * (new[0] + new[-1]) <= 3 * (sum(new[1:4])):
            k += 1

print(k)