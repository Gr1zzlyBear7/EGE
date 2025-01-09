def div(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if n // i != i:
                divs.append(n // i)
    divs = sorted(divs)
    s = 1
    if len(divs) >= 5:
        for i in range(0, 5):
            s *= divs[i]
    return len(divs) >= 5, divs, s


k = 0
for i in range(400_000_000, 100000000000000000000000):
    if div(i)[0]:
        if div(i)[2] % 100 == 17 and div(i)[2] <= i:
            print(div(i)[2], div(i)[1])