def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(1, 10000):
    tri_n = tri(n)
    if n % 3 == 0:
        tri_n = '1' + tri_n + '02(98 из 100)'
    else:
        tri_n += tri((n % 3) * 4)
    r = int(tri_n, 3)
    if r < 199:
        ans.append(n)
print(max(ans))
