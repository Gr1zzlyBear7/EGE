def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(11, 10000):
    tri_n = tri(n)
    if tri_n.count('0') + tri_n.count('2') > tri_n.count('1'):
        tri_n = '22' + tri_n
    else:
        tri_n = '11' + tri_n
    r = int(tri_n, 3)
    if r > 100:
        ans.append(r)
print(min(ans))