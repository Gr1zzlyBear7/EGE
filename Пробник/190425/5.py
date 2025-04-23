def tr(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(3, 10000):
    t = tr(n)
    if n % 3 == 0:
        t += t[-2:]
    else:
        t += tr(n % 3 * 3)
    r = int(t, 3)
    if r <= 150:
        ans.append(n)
print(max(ans))