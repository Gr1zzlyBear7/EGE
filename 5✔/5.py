def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return (new[::-1])


ans = []
for n in range(1, 1000):
    t = tri(n)
    t += str(n % 3)
    r = int(t, 3)
    if r > 100:
        ans.append(r)

print(min(ans))