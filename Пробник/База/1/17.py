data = list(map(int, open('17')))
ans = []
maxi = max([abs(x) for x in data if abs(x) % 1001 == 0])
for i in range(len(data) - 1):
    if len(str(abs(data[i]))) == 3 or len(str(abs(data[i + 1]))) == 3:
        if data[i] + data[i + 1] > maxi:
            ans.append(data[i] + data[i + 1])
print(len(ans), min(ans))