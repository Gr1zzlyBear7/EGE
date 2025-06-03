print('x y w z f')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (y == (not (w))) <= (not(w and (x == (x or (w <= z))))):
                    print(x, y, w, z, 1)
                else:
                    print(x, y, w, z, 0)
