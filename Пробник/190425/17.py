data = list(map(int, open('17.txt')))
ans = []
mini = min([x for x in data if x > 0 and len(str(x)) == 4 and x % 10 == 6])
print(mini)
for i in range(len(data) - 2):
    tri = [*data[i:i + 3]]
    c1 = [x for x in tri if len(str(abs(x))) == 4 and abs(x) % 10 == 6]
    if len(c1) == 1:
        if sum(tri) <= mini:
            ans.append(sum(tri))

print(len(ans), max(ans))