def div(n):
    s = 0
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if i % 2 == 0:
                s += i
            if n // i != i:
                divs.append(n // i)

                if (n // i) % 2 == 0:
                    s += n // i
    return s

for i in range(1204300, 1204381):
    if div(i) % 10 == 0 and div(i) != 0:
        print(i, div(i))
