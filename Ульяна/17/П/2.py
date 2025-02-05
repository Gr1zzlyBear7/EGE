data = list(map(int, open('2')))
ans = []
ma = max(x for x in data if abs(x) % 1000 == 121)
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    if sum(tri) <= ma:
        c2 = [x for x in tri if len(str(abs(x))) == 4 and abs(x) % 2 == 0]
        if len(c2) <= 1:
            ans.append(sum(tri))
print(len(ans), max(ans))