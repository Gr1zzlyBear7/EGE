def six(n):
    new = ''
    while n > 0:
        new += str(n % 6)
        n //= 6
    return new[::-1]


ans = []

for n in range(10, 1000):
    s = six(n)
    if n % 3 == 0:
        s += s[0] + s[1]
    else:
        s += six(n % 3 * 10)
    r = int(s, 6)
    if r > 680:
        ans.append(r)

print(min(ans))