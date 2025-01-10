data = [list(map(int, line.split())) for line in open('15')]

ans = []
for line in data:
    new = sorted(line)
    if new[0] ** 2 + new[1] ** 2 == new[2] ** 2:
        ans.append(new[0] + new[1])

print(max(ans))
