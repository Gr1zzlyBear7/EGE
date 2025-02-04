def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(10, 100000):
    t = tri(n)
    if n % 4 == 0:
        t += t[-3:]
    else:
        t = '1' + t + '20'
    r = int(t, 3)
    if r > 423:
        ans.append(r)
print(min(ans))