print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (x <= (z == w)) or not(y <= w):
                    pass
                else:
                    print(x, y, w, z)