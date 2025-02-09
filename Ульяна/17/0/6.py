data = list(map(int, open('6')))
ans = []
ma = max([x for x in data if abs(x) % 100 == 39 and len(str(abs(x))) == 4])
for i in range(len(data) - 1):
    dva = [*data[i:i + 2]]
    c1 = [x for x in dva if len(str(abs(x))) == 4]
    if len(c1) == 1:
        if sum(dva) ** 2 <= ma ** 2:
            ans.append(sum(dva))
print(len(ans), max(ans))