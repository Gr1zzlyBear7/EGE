def f(n):
    new = ''
    while n > 0:
        new += str(n % 5)
        n //= 5
    return int(new[::-1])


const = 125 + 25 ** 3 + 5 ** 9

print(f(const))