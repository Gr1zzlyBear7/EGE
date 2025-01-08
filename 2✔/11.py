print('x y w z')

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (y <= x) or not((x <= z) and (z <= x)) and not(w):
                    pass
                else:
                    print(x, y, w, z)

