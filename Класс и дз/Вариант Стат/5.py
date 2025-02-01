def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(1_000_000, 11_000_000):
    tri_n = tri(n)
    tri_n = tri_n.replace('2', '!').replace('0', '*')
    tri_n = tri_n.replace('!', '0').replace('*', '2')
    r = int(tri_n, 3)
    new_r = abs(n - r)
    if new_r == 1_824_648:
        ans.append(n)
print(min(ans))

