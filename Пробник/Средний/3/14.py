def six(n):
    new = ''
    while n > 0:
        new += str(n % 6)
        n //= 6
    return new[::-1]


print(six(5 * 216 ** 155 + 4 * 36 ** 156 - 4 * 6 ** 157 - 2023).count('0'))

