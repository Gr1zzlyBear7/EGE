data = list(map(int, open('17.txt')))
ans = []
ma = max([x for x in data if len(str(abs(x))) == 5 and abs(x) % 10 == 3])
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x for x in tri if abs(x) % 10 == 3]
    if c1:
        if sum(tri) <= ma:
            ans.append(sum(tri))
print(len(ans), max(ans))