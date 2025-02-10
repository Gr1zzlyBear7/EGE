data = list(map(int, open('17.txt')))
ans = []
sr = sum(data) / len(data)
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x for x in tri if x > sr]
    if len(c1) >= 2:
        ans.append(sum(tri))
print(len(ans), max(ans))