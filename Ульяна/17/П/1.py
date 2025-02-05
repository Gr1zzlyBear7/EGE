data = list(map(int, open('1')))
ans = []
mi = min(data)
ma = max(data)
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x for x in tri if x % 3 == mi % 3]
    if len(c1) == 1:
        c2 = [x for x in tri if x % 7 == ma % 7]
        if len(c2) >= 2:
            ans.append(sum(tri))
print(len(ans), max(ans))
