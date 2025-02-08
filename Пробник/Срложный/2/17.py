data = list(map(int, open('17.txt')))
ans = []
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if abs(data[i] + data[j]) % 120 == 0:
            ans.append(data[i] + data[j])
print(len(ans), max(ans))