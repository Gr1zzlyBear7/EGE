data = list(map(int, open('17')))
k = 0
ans = []
mini = min(x for x in data if x % 2025 == 0)
for i in range(len(data) - 2):
    tri = [data[i], data[i + 1], data[i + 2]]
    arr = [x for x in tri if x % mini == 0]
    if arr:
        if len(str(sum(tri))) == 6:
            ans.append(sum(tri))

print(len(ans), max(ans))