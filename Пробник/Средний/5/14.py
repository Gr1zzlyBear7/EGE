def nine(n):
    new = ''
    while n > 0:
        new += str(n % 9)
        n //= 9
    return new[::-1]


print(len([x for x in nine(2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338) if x != '0']))