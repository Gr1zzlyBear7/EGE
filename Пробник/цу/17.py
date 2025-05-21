data = list(map(int, open('17.txt')))

ans = []
mini = min([x for x in data if x > 0 and x % 110 == 0])
for i in range(len(data) - 1):
    dva = [*data[i:i + 2]]
    if sum(dva) < mini:
        ans.append((sum(dva)))
print(len(ans), max(ans))