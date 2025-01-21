data = list(map(int, open('17')))
ans = []
mini = sorted([x for x in data if 100 <= x <= 999])[1]

for i in range(len(data) - 1):
    if data[i] + data[i + 1] < mini ** 2:
        ans.append(data[i] + data[i + 1])

print(len(ans), max(ans))