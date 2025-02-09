data = list(map(int, open('9')))
ans = []
ma = max([x for x in data if len(str(abs(x))) == 4 and abs(x) % 10 == 7])
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x for x in tri if abs(x) % 10 == 7 and len(str(abs(x))) == 4]
    if len(c1) >= 2:
        if sum(tri) > ma:
            ans.append(sum(tri))
print(len(ans), max(ans))