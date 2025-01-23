def div(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if n // i != i:
                divs.append(n // i)

    return len(divs) == 2, divs


for i in range(174457, 174505 + 1):
    if div(i)[0]:
        print(div(i)[1][0], div(i)[1][1])
