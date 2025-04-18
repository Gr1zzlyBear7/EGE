def divisors(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 10 == 7 and i != 7:
                divs.append(i)
            if n // i != i:
                if (n // i) % 10 == 7 and (n // i) != 7:
                    divs.append(n // i)
    return divs


k = 0
for i in range(1_125_001, 10 ** 1000):
    if divisors(i):
        print(i, min(divisors(i)))
        k += 1
    if k == 5:
        break