data = list(map(int, open('4')))
ans = []
mi = min(data)
for i in range(len(data) - 1):
    dva = [*data[i:i + 2]]
    c1 = [x for x in dva if abs(x) % 55 == mi]
    if c1:
        ans.append(sum(dva))
print(len(ans), min(ans))