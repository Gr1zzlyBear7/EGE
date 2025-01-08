arr = []


def tf(n):
    while n > 0:
        arr.append(n % 25)
        n //= 25
    return arr[::-1]


print(tf(3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024).count(0))
