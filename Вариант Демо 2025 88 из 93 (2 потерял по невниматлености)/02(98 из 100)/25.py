def div(n):
    sm = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sm += i
            sm += n // i
            break
    return sm


k = 0
for n in range(800_000, 10 ** 100):
    if div(n) % 10 == 4:
        print(n, div(n))
        k += 1
    if k == 5:
        break