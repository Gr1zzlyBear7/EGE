def div(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 10 == 8 and i != n and i != 8:
                divs.append(i)
            if n // i != i:
                if (n // i) % 10 == 8 and (n // i) != n and (n // i) != 8:
                    divs.append(n // i)
    return divs


k = 0
for i in range(500_000, 10 ** 100):
    if div(i):
        print(i, min(div(i)))
        k += 1
    if k == 5:
        break