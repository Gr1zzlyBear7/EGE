print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (z and not w) or (z == x) or y:
                    pass
                else:
                    print(x, y, w, z)