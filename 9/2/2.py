data = [list(map(int, line.split())) for line in open('2')]
k = 0
for line in data:
    new = sorted(line)
    if new[0] + new[-1] < new[1] + new[2]:
        k += 1

print(k)
