ans = []
for n in range(100, 1000):
    num = sorted(list(str(n)))
    maxi = int(num[-1] + num[-2])
    if num[0] != '0':
       mini = int(num[0] + num[1])
    elif num[1] != '0':
        mini = int(num[1] + num[0])
    else:
        continue
    r = maxi - mini
    if r == 5:
        ans.append(n)

print(min(ans))
