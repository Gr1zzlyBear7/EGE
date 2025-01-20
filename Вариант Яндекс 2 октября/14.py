arr = []


def forty_nine(n):
    n = abs(n)
    while n > 0:
        arr.append(n % 49)
        n //= 49
    return sum(arr)


print(forty_nine(18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50))