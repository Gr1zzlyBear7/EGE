ans = []
for n in range(1000, 10000):
    num = str(n)
    r = int(''.join([str(x) for x in sorted([int(num[0]) * int(num[1]), int(num[2]) * int(num[3])])]))
    if r == 1214:
        ans.append(n)

print(max(ans))

