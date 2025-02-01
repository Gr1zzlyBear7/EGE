data = list(map(int, open('17.txt')))
ans = []
mini = min(data)
maxi = max(data)
for i in range(len(data) - 2):
    tri = [data[i], data[i + 1], data[i + 2]]
    c1 = [x for x in tri if len(str(x)) == 4]
    if c1:
        c2 = [x for x in tri if (x % 5) == (mini % 5)]
        if len(c2) <= 1:
            c3 = [x for x in tri if (x % 7) == (maxi % 7)]
            if len(c3) >= 2:
                ans.append(sum(tri))
print(len(ans), max(ans))
