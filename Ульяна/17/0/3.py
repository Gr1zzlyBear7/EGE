data = list(map(int, open('3')))
ans = []
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x for x in tri if abs(x) % 12 == 0]
    if c1:
        c2 = [x for x in tri if abs(x) % 3 == 0]
        if len(c2) == 3:
            ans.append(sum(tri) / 3)
print(len(ans), min(ans))