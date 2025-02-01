def five(n):
    new = ''
    while n > 0:
        new += str(n % 5)
        n //= 5
    return new[::-1]


ans = []
for n in range(1, 1_000_000):
    five_n = five(n)
    if int(five_n[-1]) % 2 == 0:
        five_n = five_n + '2'
    else:
        five_n = '2' + five_n + '3'
    r = int(five_n, 5)
    if r < 1000:
        ans.append(n)
print(max(ans))
