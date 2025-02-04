data = list(map(int, open('17.txt')))
ans = []
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    if abs(sum(tri)) % 2022 == 0:
        if len([x for x in tri if x >= 0]) >= 1:
            ans.append(sum(tri))
print(len(ans), max(ans))
