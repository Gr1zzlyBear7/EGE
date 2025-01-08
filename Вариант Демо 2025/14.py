def sev(n):
    new = ''
    while n > 0:
        new += str(n % 7)
        n //= 7
    return int(new[::-1])


const = 7 ** 170 + 7 ** 100

for x in range(2030, -1, -1):
    new = sev(x)
    if str(sev(const - x)).count('0') == 71:
        print(x)
        print(str(sev(const - x)).count('0'))
        break