def nine(n):
    new = ''
    while n > 0:
        new += str(n % 9)
        n //= 9
    return new


const = 9 ** 2025 + 9 ** 1000
for x in range(5769, -1, -1):
    if nine(const - x).count('0') == 1026:
        print(x)
        break