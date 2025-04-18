data = list(map(int, open('17.txt')))
neg = sum([x for x in data if x < 0])
ans = []
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    if max(tri) * min(tri) > neg:
        ans.append((sum(tri)))
print(len(ans), max(ans))