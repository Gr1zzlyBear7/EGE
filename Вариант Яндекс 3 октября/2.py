print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if c and (a or d) and (d <= b):
                    print(a, b, c, d)