def five(n):
    new = ''
    while n > 0:
        new += str(n % 5)
        n //= 5
    return len(new) <= 4


k = 0
for n in range(1, 100000):
    if five(n) and len(bin(n)[2:]) >= 5 and n % 16 == 12:
        k += 1

print(k)