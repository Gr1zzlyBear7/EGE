def f(n):
    new = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            new.append(i)
            if n // i != i:
                new.append(n // i)
    return sum(new)


k = 0
for i in range(500_000, 10 ** 1000):
    const = f(i)
    if const % 10 == 6:
        print(i, const)
        k += 1
    if k == 5:
        break