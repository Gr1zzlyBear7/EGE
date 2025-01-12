def div(n):
    sm = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sm += i
            if n // i != i:
                sm += (n // i)
                return sm


k = 0
for x in range(800001, 10 ** 1000):
    try:
        if div(x) % 10 == 4:
            k += 1
            print(x, div(x))
        if k == 4:
            break
    except:
        pass