print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a and b) <= c) and ((b and c) <= d):
                    pass
                else:
                    print(a, b, c, d)