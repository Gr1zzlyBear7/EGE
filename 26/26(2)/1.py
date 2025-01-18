s = 100000
n = 1000

data = sorted(list(map(int, open('1.txt'))))
arr = []

while s >= sum(arr) + data[0]:
    arr.append(data.pop(0))

for i in range(len(data)):
    if sum(arr) - arr[-1] + data[i] <= s:
        arr[-1], data[i] = data[i], arr[-1]

print(len(arr), arr[-1])