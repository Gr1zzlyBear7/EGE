def sev(n):
    new = ''
    while n > 0:
        new += str(n % 7)
        n //= 7
    return new[::-1]


const = 7 ** 91 + 7 ** 160
for x in range(2030, -1, -1):
    if sev(const - x).count('0') == 70:
        print(x)
        break