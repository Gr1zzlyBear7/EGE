data = list(map(int, open('17.txt')))
ans = []
mini = min([x for x in data if len(str(abs(x))) == 3 and abs(x) % 100 == 15])
for i in range(len(data) - 2):
    tri = data[i:i+3]
    c1 = [x > 0 for x in tri]
    c2 = [x < 0 for x in tri]
    if all(c2) or all(c1):
        if max(tri) * min(tri) > mini ** 2:
            ans.append(max(tri) * min(tri))

print(len(ans), min(ans))