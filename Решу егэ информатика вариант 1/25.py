def ez(n):
    k = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2:
                k += 1
            if n // i != i:
                if (n // i) % 2:
                    k += 1
    return k


for i in range(35_000_000, 40_000_000 + 1):
    if ez(i) == 5:
        print(i)
