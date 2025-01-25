data = list(map(int, open('17')))
ans = []
mini = min(data)
for i in range(len(data) - 1):
    if data[i] % 27 == mini or data[i + 1] % 27 == mini:
        ans.append(data[i] + data[i + 1])
print(len(ans), max(ans))
