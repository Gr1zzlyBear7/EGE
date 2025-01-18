def five(x):
    new = ''
    while x > 0:
        new += str(x % 5)
        x //=5
    return (new[::-1])


const = 25 ** 61 + 5 ** 178
for x in range(2042, 0, -1):
    if five(const - x).count('0') == 60:
        print(x, five(const - x))
        break