def div(n):
    divs = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                divs.append(i)
            if n // i != i:
                if (n // i) % 2 == 0:
                    divs.append(n // i)
    return len(divs) == 4, sorted(divs)


k = 0
for i in range(190201, 190261):
    if div(i)[0]:
        print(div(i)[1])