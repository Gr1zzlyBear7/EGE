print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((1 == w) == (not ((w and x) or y))) <= z:
                    print(x, y, w, z, True)
                else:
                    print(x, y, w, z, False)
