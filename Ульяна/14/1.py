arr = []


def fif(n):
    n = abs(n)
    while n > 0:
        arr.append(n % 15)
        n //= 15
    return len(set(arr))


print(fif(11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338))