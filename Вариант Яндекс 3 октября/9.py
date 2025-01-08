data = [list(map(int, line.split('\t'))) for line in open('9').readlines()]

ans = []
k = 0
for line in data:
    if len(set(line)) == 4:
        new = sorted(line)
        if (new[0] + new[-1]) / 2 <= (new[1] + new[2]) / 2:
            k += 1
print(k)