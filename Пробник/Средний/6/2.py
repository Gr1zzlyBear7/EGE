print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if w and (not (not y or x) or z):
                    print(x, y, w, z, True)
                else:
                    print(x, y, w, z, False)

