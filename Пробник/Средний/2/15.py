a = 1 # 1 т.к. наиб
f_usl = 1
for x in [k * 0.25 for k in range(-10000, 10000)]:
    p = 15 <= x <= 33
    q = 35 <= x <= 48
    f = ((a) and (not q)) <= ((p) or (q))
    if f == f_usl:
        print(x)
print(33 - 15, 48 - 35)