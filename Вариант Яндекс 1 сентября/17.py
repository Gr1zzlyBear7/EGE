data = list(map(int, open('17 (8).txt')))
k = 0
ans = []
cou = len([x for x in data if abs(x) % 2042 == 0])
for i in range(len(data) - 1):
    if data[i] + data[i + 1] > cou:
        ans.append(data[i] + data[i + 1])

print(len(ans), max(ans))