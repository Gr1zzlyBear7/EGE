data = list(map(int, open('17').readlines()))

ans = []
k = 0

for i in range(len(data) - 2):
    a, b, c = data[i], data[i + 1], data[i + 2]
    arr = sorted([a, b, c])
    if arr[2] ** 2 < arr[0] ** 2 + arr[1] ** 2:
        ans.append(a + b + c)
print(len(ans), max(ans))

