data = list(map(int, open('17.txt')))
ans = []
for i in range(len(data) - 1):
    if abs(data[i] + data[i + 1]) % 2 == 0 and abs(data[i] + data[i + 1]) % 10 != 6:
        ans.append((data[i] + data[i + 1]) / 2)
print(len(ans), max(ans))