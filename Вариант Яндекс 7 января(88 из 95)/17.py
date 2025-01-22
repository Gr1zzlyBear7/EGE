data = list(map(int, open('17')))
ans = []
maxi = max([x for x in data if 100 <= x <= 999])
for i in range(len(data) - 1):
    s1 = sum(list(map(int, str(abs(data[i])))))
    s2 = sum(list(map(int, str(abs(data[i + 1])))))
    if (s1 % 5 == 0 and s2 % 5 != 0) or (s1 % 5 != 0 and s2 % 5 == 0):
        if abs(data[i] ** 2 - data[i + 1] ** 2) >= maxi ** 3:
            ans.append(data[i] + data[i + 1])
print(len(ans), max(ans))