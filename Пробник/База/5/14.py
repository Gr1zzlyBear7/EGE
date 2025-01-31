def six(n):
    new = ''
    while n > 0:
        new += str(n % 6)
        n //= 6
    return new


print(sum(map(int, six(5 * 216 ** 3031 + 4 * 36 ** 3042 - 3 * 6 ** 3053 - 3064))))