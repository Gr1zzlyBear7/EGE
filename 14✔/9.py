def six(n):
    new = ''
    while n > 0:
        new += str(n % 6)
        n //= 6
    return int(new[::-1])


const = 36 ** 17 + 71
for x in range(1, 2000):
    if sum(map(int, str(six(const - 6 ** x)))) == 61:
        print(x)
        break