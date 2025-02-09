data = list(map(int, open('10')))
ans = []
mi = min(data)
for i in range(len(data) - 1):
    dva = [*data[i:i + 2]]
    if (dva[0] % 77) * (dva[1] % 77) == mi ** 2:
        ans.append(dva[0] * dva[1])
print(len(ans), min(ans))