def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


ans = []
for n in range(1, 1000):
    t_n = tri(n)
    if n % 3 == 0:
        t_n += t_n[-2:]
    else:
        t_n += tri(sum(map(int, t_n)))
    r = int(t_n, 3)
    if r % 2 == 0 and r > 220:
        ans.append(r)
print(min(ans))