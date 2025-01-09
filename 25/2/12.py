def div(n):
    div = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 10 == 7:
                div.append(i)
            if (n // i) != i:
                if (n // i) % 10 == 7:
                    div.append((n // i))
    return len(div) == 3, div


k = 0
for i in range(550_000, 10 ** 1000):
    if div(i)[0]:
        print(i, max(div(i)[1]))
        k += 1
    if k == 5:
        break