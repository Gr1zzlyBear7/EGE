data = list(map(int, open('2')))
ans = []
for i in range(len(data) - 1):
    if abs(data[i]) % 7 == 0 or abs(data[i + 1]) % 7 == 0:
        if abs(data[i] + data[i + 1]) % 5 == 0:
            ans.append(data[i] + data[i + 1])
print(len(ans), max(ans))