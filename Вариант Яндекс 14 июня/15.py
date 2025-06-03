a = 0
f_usl = 0
for x in [k * 0.25 for k in range(-10000, 10000)]:
    b = 1 <= x <= 9999
    c = 3648 <= x <= 6287
    f = ((b) == (c)) or (a) or (x > 4200)
    if f != f_usl:
        print(x)