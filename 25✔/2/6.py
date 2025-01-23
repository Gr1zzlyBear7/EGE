def div(n):
    divs = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.append(i)
            if n // i != 0:
                divs.append(n // i)

    return int(sum(divs) / len(divs)) if divs else 0

print(div(16))
k = 0
for i in range(550000, 1000000000000):
    if div(i) % 31 == 13:
        k += 1
        print(i, div(i))
    if k == 5:
        break