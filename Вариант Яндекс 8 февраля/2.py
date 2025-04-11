print('x y w')
for x in range(2):
    for y in range(2):
        for w in range(2):
            if (x <= y) and (w or (not w)):
                print(x, y, w, True)
            else:
                print(x, y, w, False)
