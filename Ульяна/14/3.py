def five(n):
    new = ''
    while n > 0:
        new += str(n % 5)
        n //= 5
    return new


const = 5 ** 2025 + 5 ** 400
arr = []
for x in range(70_000, 9, -1):
    r = five(const - x).count('4')
    if r == 399:
        print(r, x)
