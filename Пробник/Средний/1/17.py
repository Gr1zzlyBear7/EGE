data = list(map(int, open('17')))
ans = []
const = sum([sum(list(map(int, str(x)))) for x in data if abs(x) % 35 == 0])
for i in range(len(data) - 1):
    if data[i] > const > data[i + 1]:
        if hex(data[i + 1])[2:][-2:] == 'ef':
            ans.append(data[i] + data[i + 1])
    elif data[i + 1] > const > data[i]:
        if hex(data[i])[2:][-2:] == 'ef':
            ans.append(data[i] + data[i + 1])

print(len(ans), min(ans))