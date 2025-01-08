def four(n):
    new = ''
    while n > 0:
        new += str(n % 4)
        n //= 4
    return new[::-1]


print(four(3 * 16 ** 8 - 4 ** 5 + 3).count('3'))