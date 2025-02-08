def four(n):
    new = ''
    while n > 0:
        new += str(n % 4)
        n //= 4
    return new[::-1]


const = 43 ** 56 + 113 ** 841
for x in range(2005, -1, -1):
    arr = four(const - x)
    c1 = [z for z in arr if int(z) % 2 == 0]
    c2 = [z for z in arr if int(z) % 2 == 1]
    if len(c1) % 2 == len(c2) % 2 == 0 and arr.count('2') <= 712:
        print(x)
        break