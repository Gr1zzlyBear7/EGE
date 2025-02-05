data = list(map(int, open('7')))
ans = []
mi = min(x for x in data if abs(x) % 10 == 7)
for i in range(len(data) - 1):
    dva = [*data[i:i + 2]]
    c1 = [abs(x) % 10 for x in dva]
    if len(set(c1)) == 1:
        c2 = [x for x in dva if abs(x) % 7 == 0]
        if len(c2) == 1:
            if dva[0] ** 2 + dva[1] ** 2 <= mi ** 2:
                ans.append(dva[0] ** 2 + dva[1] ** 2)
print(len(ans), max(ans))