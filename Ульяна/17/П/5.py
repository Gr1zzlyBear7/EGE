data = list(map(int, open('5')))
ans = []
ma = max(x for x in data if abs(x) % 100 == 17)
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x for x in tri if len(str(abs(x))) == 4]
    if len(c1) == 2:
        c2 = [x for x in tri if abs(x) % 5 == 0]
        if c2:
            if sum(tri) > ma:
                ans.append(sum(tri))
print(len(ans), max(ans))