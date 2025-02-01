def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(1, 1000):
    t = tri(n)
    if n % 3 == 0:
        t += t[-2:]
    else:
        t += tri((n % 3) * 5)
    r = int(t, 3)
    if r > 133:
        ans.append(r)
print(min(ans))