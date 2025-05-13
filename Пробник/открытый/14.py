def sev(n):
    new = ''
    while n > 0:
        new += str(n % 7)
        n //= 7
    return new[::-1]


const = 7 ** 350 + 7 ** 150
for x in range(2300, -1, -1):
    if sev(const - x).count('0') == 200:
        print(x)
        break