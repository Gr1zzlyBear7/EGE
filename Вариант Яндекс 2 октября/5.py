def five(n):
    new = ''
    while n > 0:
        new += str(n % 5)
        n //= 5
    return new[::-1]


ans = []
for n in range(1, 1000):
    five_n = five(n)
    if n % 25 == 0:
        five_n += five_n[-3:]
    else:
        five_n += five(n % 25)
    r = int(five_n, 5)
    if r > 10000:
        ans.append(n)

print(min(ans))