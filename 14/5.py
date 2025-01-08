def five(n):
    new = ''
    while n > 0:
        new += str(n % 5)
        n //= 5
    return new[::-1]


const = 125 ** 200 + 74

for x in range(1, 1000):
    if five(const - 5 ** x).count('4') == 100:
        print(x)
        break