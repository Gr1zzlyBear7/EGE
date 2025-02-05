print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((x <= y) or not (z <= w)) and ((w <= (not x)) or (not y <= z)):
                    pass
                else:
                    print(x, y, w, z)