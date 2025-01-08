def eight(n):
    new = ''
    while n > 0:
        new += str(n % 8)
        n //= 8
    return new[::-1]


print(eight(64 ** 30 + 2 ** 300 - 4).count('7'))