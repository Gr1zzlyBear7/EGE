al = '0123456789abcde'


def fifteen(n):
    new = ''
    while n > 0:
        new += al[n % 15]
        n //= 15
    return new[::-1]


print(len(set(fifteen(11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338))))