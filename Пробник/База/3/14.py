def eight(n):
    new = ''
    while n > 0:
        new += str(n % 8)
        n //= 8
    return new.count('7')


print(eight(64 ** 150 + 4 ** 300 - 32))