def f(x, a):
    b = [-42, -10, -8, 2, 16]
    c = [-10, -4, 2, 15, 23]
    return ((x in a) <= (x in b)) or (x in c)


for a in range(-100, 100):
    if all([f(x, [a]) for x in range(-100, 100)]):
        print(a)