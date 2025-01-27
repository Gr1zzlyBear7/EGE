arr = []


def f(n):
    while n > 0:
        arr.append(n % 32)
        n //= 32
    return arr


print(f(3 * 1024 ** 75 + 2 * 256 ** 76 - 16 ** 77 - 2023).count(0))

