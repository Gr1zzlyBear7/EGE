print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((w <= y) or not(y <= z)) and not(x) and (x != z):
                    print(x, y, w, z)