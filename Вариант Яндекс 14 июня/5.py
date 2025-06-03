def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for x in range(1, 10000):
    t = sorted(tri(x), reverse=True)
    t += t[0]
    r = int(''.join(t), 3)
    if r < 1200:
        ans.append(r)
print(max(ans))