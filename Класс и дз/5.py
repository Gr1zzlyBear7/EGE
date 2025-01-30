def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(1, 1000):
    tri_n = tri(n)
    if n % 3 == 0:
        tri_n += tri_n[-2:]
    else:
        tri_n += tri((n % 3) * 5)
    r = int(tri_n, 3)
    if r > 133:
        ans.append(r)
print(min(ans))