def six(n):
    new = ''
    while n > 0:
        new += str(n % 6)
        n //= 6
    return new


def five(n):
    new = ''
    while n > 0:
        new += str(n % 5)
        n //= 5
    return new


for n in range(1, 1000):
    if len(six(n)) == 2 and len(five(n)) == 3 and n % 11 == 1:
        print(n)