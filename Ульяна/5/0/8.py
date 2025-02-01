def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(1, 10000):
    t = tri(n)
    sm = sum(map(int, t))
    if sm % 4 == 0:
        t = '1' + t[:-2]
    else:
        t += tri((sm % 4) * 3)
    r = int(t, 3)
    if r > 353:
        ans.append(r)
print(min(ans))