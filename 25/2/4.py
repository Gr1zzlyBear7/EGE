def div(n):
    s = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i
            if n // i != i:
                s += n // i
    return s


k = 0
for i in range(150000, 10000000000000000000):
    if div(i) % 13 == 10:
       print(i, div(i))
       k += 1
    if k == 7:
        break