def seven(n):
    new = ''
    while n > 0:
        new += str(n % 7)
        n //= 7
    return new


print(sum(map(int, seven(51 * 7 ** 12 - 7 ** 3 - 22))))