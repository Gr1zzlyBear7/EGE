data = list(map(int, open('17')))
ans = []
for i in range(2, len(data) - 3):
    if 0 < (data[i + 3] + data[i + 2]) <= (data[i - 2] + data[i - 1]) < (data[i] + data[i + 1]):
        ans.append(data[i] * data[i + 1])
print(len(ans), min(ans))
