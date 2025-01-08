ans = []

n = 120
for m in range(1, 1000):
    pn1 = 2
    pm2 = 1

    for x in str(m):
        if int(x) != 0:
            if int(x) % 2 == 0:
                pn1 *= int(x)
            else:
                pm2 *= int(x)

    r = abs(pn1 - pm2)
    if r == 29:
        print(m)
        break