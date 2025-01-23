def div(n):
    divs = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if n // i != i:
                divs.append(n // i)
    return len(divs) == 4, divs

for i in range(154026, 154043):
    if div(i)[0]:
        print(div(i)[1])