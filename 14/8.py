al = '0123456789ab'


def twelve(n):
    new = ''
    while n > 0:
        new += al[n % 12]
        n //= 12
    return new[::-1]

print(twelve(6 * 144 ** 26 + 11 * 12 ** 75 - 48).count('b'))