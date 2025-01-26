def four(n):
    new = ''
    while n > 0:
        new += str(n % 4)
        n //= 4
    return new[::-1]


ans = []
for n in range(1, 1000):
    four_n = four(n)
    if n % 4 == 0:
        four_n = '2' + four_n + '03'
    else:
        four_n = four_n + four((n % 4) * 5)
    r = int(four_n, 4)
    if r <= 567:
        ans.append(n)
print(ans)
print(max(ans))