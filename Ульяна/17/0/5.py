data = list(map(int, open('5')))
ans = []
mi = min([x for x in data if x % 17 == 0])
for i in range(len(data) - 1):
    dva = [*data[i:i + 2]]
    c1 = [x for x in dva if x % mi == 0]
    if c1:
        ans.append(sum(dva))
print(len(ans), max(ans))