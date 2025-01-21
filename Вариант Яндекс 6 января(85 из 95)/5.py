ans = []
for n in range(1000, 10000):
    if len(set(str(n))) == 4:
        num = sorted(str(n))
        n1 = int(num[0]) + int(num[-1])
        n2 = int(num[1]) * int(num[2])
        if n1 > n2:
            new = int(str(n2) + str(n1))
        else:
            new = int(str(n1) + str(n2))
        r = int(new)
        if r > 85:
            ans.append(n)
print(min(ans))