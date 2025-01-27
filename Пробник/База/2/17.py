data = list(map(int, open('17')))
ans = []
mini = min([x for x in data if x % 21 == 0])
for i in range(len(data) - 1):
    if data[i] % mini == 0 or data[i + 1] % mini == 0:
        ans.append(data[i] + data[i + 1])

print(len(ans), max(ans))