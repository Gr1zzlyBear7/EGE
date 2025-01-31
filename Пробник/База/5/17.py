data = list(map(int, open('17.txt')))
ans = []
for i in range(len(data) - 1):
    if data[i] * data[i + 1] > 0:
        if abs(data[i] + data[i + 1]) % 7 == 0:
            ans.append(data[i] * data[i + 1])
print(len(ans), min(ans))