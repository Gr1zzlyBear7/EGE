data = list(map(int, open('6')))
ans = []
mi = min(x for x in data if len(str(abs(x))) == 2)
ma = max(x for x in data if abs(x) % 10 == 1 and len(str(abs(x))) == 4)
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x > mi ** 2 for x in tri]
    if c1.count(True) == 2:
        if (abs(tri[0]) * abs(tri[1]) * abs(tri[2])) % ma == 0:
            ans.append(abs(tri[0]) + abs(tri[1]) + abs(tri[2]))
print(len(ans), max(ans))