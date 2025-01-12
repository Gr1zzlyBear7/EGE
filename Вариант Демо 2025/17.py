data = list(map(int, open('17.txt')))

ans = []
mini = min(data)
for i in range(len(data) - 1):
    if data[i] % 16 == mini or data[i + 1] % 16 == mini:
        ans.append(data[i] + data[i + 1])

print(len(ans), max(ans))