a = 0 # т.к. наим длину
f_usl = 1
for x in [k * 0.25 for k in range(-10000, 10000)]:
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    f = p <= (((q) and not a) <= (not p))
    if f != f_usl: # т.к. условие наим
        print(x)