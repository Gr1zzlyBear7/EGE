def four(n):
    new = ''
    while n > 0:
        new += str(n % 4)
        n //= 4
    return int(new[::-1])


for i in range(199, 0, -1):
    if four(i) % 1000 == 123:
        print(i)