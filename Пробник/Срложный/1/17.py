data = list(map(int, open('17.txt')))
ans = []
mi = min([x for x in data if x % 10 == 4])
ma = max([x for x in data if x % 10 == 4])
for i in range(len(data) - 1):
    if data[i] + data[i + 1] < ma + mi:
        ans.append(data[i] + data[i + 1])
print(len(ans), max(ans))