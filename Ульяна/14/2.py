def seven(n):
    new = ''
    while n > 0:
        new += str(n % 7)
        n //= 7
    return new[::-1]


arr = (list(seven(5 * 343 ** 8 + 4 * 49 ** 12 + 7 ** 14 - 98)))
print(arr)