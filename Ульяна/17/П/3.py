data = list(map(int, open('3')))
ans = []
odds = [x for x in data if abs(x) % 2 != 0]
sr = sum(odds) / len(odds)
for i in range(len(data) - 1):
    dva = [*data[i:i + 2]]
    c1 = [x for x in dva if abs(x) % 100 == 11]
    if len(c1) == 1:
        if sum(dva) >= sr:
            ans.append(sum(dva))
print(len(ans), max(ans))