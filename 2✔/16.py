print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not(z and not w) or ((z <= w) == (x <= y)):
                    pass
                else:
                    print(x, y, w, z)