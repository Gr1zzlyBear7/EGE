print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((w == 1) <= z) and ((not y) and x):
                    print(x, y, w, z, True)
                else:
                    print(x, y, w, z, False)

