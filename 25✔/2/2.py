def div(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if n // i != i:
                divs.append(n // i)
    return len(divs) == 3, divs


for i in range(81234, 134689 + 1):
    if div(i)[0]:
        for i in (sorted(div(i)[1])):
            print(i, end=' ')
        print()