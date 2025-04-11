def tri(n):
    if n == 0:
        return '0'
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(1, 100000):
    t = tri(n)
    t += tri(t.count('2'))
    t += tri(t.count('1'))
    t += tri(t.count('0'))
    r = int(t, 3)
    if r < 1000:
        ans.append(n)
print(max(ans))