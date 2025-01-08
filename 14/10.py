def six(n):
    new = ''
    while n > 0:
        new += str(n % 6)
        n //= 6
    return new[::-1]


num = six(5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875)

print(num.count('5') - num.count('0'))