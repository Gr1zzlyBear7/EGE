data = list(map(int, open('17.txt')))
maxi = max([x for x in data if x > 0 and len(str(x)) == 4])
ans = []
for i in range(len(data) - 1):
    dva = [*data[i: i + 2]]
    if abs(dva[0] - dva[1]) >= maxi:
        ans.append(sum(dva))

print(len(ans), max(ans))