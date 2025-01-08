def three(n):
    new = ''
    while n > 0:
        new += str(n % 3)
        n //= 3
    return new[::-1]


print(three(2 * 27 ** 7 + 3 ** 10 - 9).count('0'))