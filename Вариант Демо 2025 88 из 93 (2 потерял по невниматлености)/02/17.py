data = list(map(int, open('17.txt')))
ans = []
mi = min(data)
for i in range(len(data) - 1):
    dva = [*data[i:i + 2]]
    if dva[0] % 16 == mi or dva[1] % 16 == mi:
        ans.append(sum(dva))
print(len(ans), max(ans))