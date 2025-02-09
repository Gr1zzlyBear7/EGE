def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(1, 10000):
    t = tri(n)
    if n % 3 == 0:
        t = '1' + t + '02(98 из 100)'
    else:
        t += tri((n % 3) * 4)
    r = int(t, 3)
    if r < 199:
        ans.append(n)
print(max(ans))