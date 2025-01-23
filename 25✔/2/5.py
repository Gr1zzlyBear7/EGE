def div(n):
    sm = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sm += i
            sm += n // i
            return sm


k = 0
for i in range(250200, 100000000):
    try:
        if div(i) % 123 == 17:
            print(i, div(i))
            k += 1
        if k == 5:
            break
    except:
        pass