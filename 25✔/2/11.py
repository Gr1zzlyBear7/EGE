def div(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 3 == 0:
                divs.append(i)
            if n // i != i:
                if (n // i) % 3 == 0:
                    divs.append(n // i)
    return len(divs) == 5, divs


k = 0
for i in range(300_000, 10 ** 100):
    if div(i)[0]:
        print(i, max(div(i)[1]))
        k += 1
    if k == 4:
        break