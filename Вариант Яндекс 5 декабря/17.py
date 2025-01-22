data = list(map(int, open('17')))

k = 0
ans = []
choco_min = min([x for x in data if x > 0 and x % 2025 == 0])
for i in range(len(data) - 3):
    four = [data[i], data[i + 1], data[i + 2], data[i + 3]]
    if four[0] > 0 and four[-1] > 0:
        if abs(four[1] - four[2]) <= choco_min:
            ans.append(sum(four))

print(len(ans), min(ans))