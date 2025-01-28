a = 0
f_usl = 1
for x in [k * 0.25 for k in range(-10000, 10000)]:
    b = 10 <= x <= 23
    c = 12 <= x <= 30
    f = not b or a or not c
    if f_usl != f:
        print(x)