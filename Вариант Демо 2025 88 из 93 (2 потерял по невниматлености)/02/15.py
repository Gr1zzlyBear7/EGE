a = 0 # т.к. наим длину иначе 1
f_usl = 1
for x in [k * 0.25 for k in range(-10000, 10000)]:
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    f = p <= (((q) and (not a)) <= (not p))
    if f != f_usl: # т.к. наим ставим не равно
        print(x)