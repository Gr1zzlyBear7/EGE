ans = []
for n in range(100, 1000):
    num = str(n)
    r = int(''.join([str(x) for x in sorted([int(num[0]) ** 2 + int(num[1]) ** 2, int(num[1]) ** 2 + int(num[2]) ** 2], reverse=True)]))
    if r == 9010:
        ans.append(n)

print(min(ans))

