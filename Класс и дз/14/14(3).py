def six(n):
    new = ''
    while n > 0:
        new += str(n % 6)
        n //= 6
    return new[::-1]


const = 6 ** 260 + 6 ** 160 + 6 ** 60
for x in range(2030):
    if six(const - x).count('0') == 202:
        print(x)
        break
