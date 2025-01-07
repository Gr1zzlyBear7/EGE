data = list(map(int, open('7936').readlines()))

ans = []

maxi = max([x for x in data if len(str(abs(x))) == 5 and abs(x) % 100 == 43])

for i in range(len(data) - 2):
    tri = data[i:i + 3]
    if [x for x in tri if len(str(abs(x))) == 5 and abs(x) % 100 == 43]:
        if tri[0] ** 2 + tri[1] ** 2 + tri[2] ** 2 <= maxi ** 2:
            ans.append(tri[0] ** 2 + tri[1] ** 2 + tri[2] ** 2)
print(len(ans), min(ans))
