def f(n):
    new = ''
    while n > 0:
        new += str(n % 5)
        n //= 5
    return new


print(f(7 * 5 ** 123 + 6 * 5 ** 111 - 5 * 25 ** 50 + 4 * 125 ** 30 - 3 * 5 ** 10).count('4'))