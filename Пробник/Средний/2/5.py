def four(n):
    new = ''
    while n > 0:
        new += str(n % 4)
        n //= 4
    return new[::-1]


ans = []
for n in range(1, 10000):
    f = four(n)
    if len(f) % 2 == 0:
        f = f[:len(f) // 2] + '0' + f[len(f) // 2]
    else:
        pass
    r = int(f)
    if r <= 180:
        ans.append(n)
print(max(ans))