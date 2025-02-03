data = list(map(int, open('17.txt')))
ans = []
ma = max([x for x in data if abs(x) % 100 == 31])
mi = min([x for x in data if abs(x) % 100 == 31])
c = abs(ma + mi)
for i in range(len(data) - 1):
    if data[i] > c and data[i + 1] > c:
        ans.append(data[i] + data[i + 1])
print(len(ans), max(ans))