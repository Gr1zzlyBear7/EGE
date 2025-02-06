ans = []
for n in range(1, 10000):
    s = 1
    for x in str(n):
        s *= int(x)
    b = bin(s)[2:]
    b += '00'
    r = int(b, 2)
    if r == 864:
        if len(set(str(n))) == 1:
            print(n)