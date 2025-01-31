def tri(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]

const = 3 ** 100
for x in range(2030, -1, -1):
    if tri(const - x).count('0') == 5:
        print(x)
        break