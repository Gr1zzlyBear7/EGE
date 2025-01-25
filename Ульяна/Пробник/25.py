def divs(n):
    div = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 10 == 7 and i != 7:
                div.append(i)
            if (n // i) != i:
                if (n // i) % 10 == 7 and (n // i) != 7:
                    div.append(n // i)
    return min(div) if div else False

k = 0
for i in range(700_000, 10 ** 100):
    if divs(i):
        print(i, divs(i))
        k += 1
    if k == 5:
        break