def four(n):
    new = ''
    while n > 0:
        new += str(n % 4)
        n //= 4
    return new[::-1]


ans = []
for n in range(1, 1000):
    four_n = four(n)
    if n % 3 == 0:
        four_n = four_n[-1] + four_n + four_n[0] + '1'
    else:
        four_n += four(n % 3)
    r = int(four_n, 4)
    if r <= 340:
        ans.append(r)
print(max(ans))