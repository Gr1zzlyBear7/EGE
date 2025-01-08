data = list(map(int, open('17').readlines()))

ans = []
maxi = max([x for x in data if 1000 <= x <= 9999 and x % 100 == 42])
for i in range(len(data) - 2):
    tri = data[i:i + 3]
    if len([x for x in tri if abs(x) % 100 == 42 and 1000 <= abs(x) <= 9999]) >= 2:
        if sum(tri) > maxi:
            print(tri, maxi)
            ans.append(sum(tri))
print(len(ans), max(ans))