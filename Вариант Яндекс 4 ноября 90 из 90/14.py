con = 16 ** 560 + 16 ** 120
for x in range(401, 10 ** 1000):
    if hex(con - x)[2:].count('0') == 442:
        print(x)
        break