ans = []
for n in range(100, 1000):
    num = str(n)
    r = int(''.join([str(x) for x in sorted([int(num[0]) * int(num[1]), int(num[1]) * int(num[2])], reverse=True)]))
    if r == 240:
        ans.append(n)

print(max(ans))

