data = list(map(int, open('17.txt')))
ans = []
ma = max([x for x in data if str(abs(x))[-2:] == '09'])
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x for x in tri if abs(x) % 7 == 0]
    if len(c1) == 2:
        if sum(tri) < ma:
            ans.append(tri[0] * tri[1] * tri[2])
print(len(ans), min(ans))