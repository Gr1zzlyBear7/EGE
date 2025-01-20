def divs(num):
    divs = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i % 10 == 7 and i != 7:
                divs.append(i)
            if num // i != i:
                if (num // i) % 10 == 7 and (num // i) != 7:
                    divs.append(num // i)
    return divs


k = 0
for i in range(700000, 10**1000):
    if divs(i):
        print(i, min(divs(i)))
        k += 1
    if k == 5:
        break