m = 100000
data = [x.split() for x in open('15')]
data.sort(key=lambda x: (int(x[0]), x[1]))
for i in data:
    print(i)
total = 0
arr = []
while sum(arr) + int(data[0][0]) <= m:
    if data[0][1] == 'A':
        total += 1
    value = data.pop(0)
    arr.append(int(value[0]))
for i in range(len(data)):
    if sum(arr) - arr[-1] + int(data[i][0]) <= m:
        if data[i][1] == 'A':
            total += 1
        arr[-1], data[i][0] = int(data[i][0]), arr[-1]
print(m - sum(arr), total)