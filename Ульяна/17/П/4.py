data = list(map(int, open('4')))
ans = []
mi = min(x for x in data if abs(x) % 100 == 25)
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x for x in tri if len(str(abs(x))) == 4]
    if len(c1) >= 2:
        if tri[0] * tri[1] * tri[2] <= mi ** 2:
            ans.append(tri[0] * tri[1] * tri[2])
print(len(ans), max(ans))