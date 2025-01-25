def nine(n):
    new = ''
    while n > 0:
        new += str(n % 9)
        n //= 9
    return abs(new.count('2') - new.count('8'))


const = 9 ** 1942 + 9 * 6 ** 971 + 214
for x in range(1, 1000):
    if nine(const - x) == 471:
        print(x)