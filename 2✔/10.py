print('x y z f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x == (y <= z)):
                print(x, y, z, 1)
            else:
                print(x, y, z, 0)


