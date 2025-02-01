def sev(n):
    new = ''
    while n > 0:
        new += str(n % 7)
        n //= 7
    return new[::-1]


ans = []
for n in range(1, 10000):
    sev_n = sev(n)
    if sev_n.count('2') % 2 == 0:
        sev_n += '555'
    else:
        sev_n = '1' + sev_n
    r = int(sev_n, 7)
    if r < 3799:
        ans.append(n)
print(max(ans))