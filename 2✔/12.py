print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not(w) and (not(y or z) or x and y):
                    print(x, y, w, z)

