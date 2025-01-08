for x in range(0, 12):
    k = int(f'3364{x}', 11) + int(f'{x}7946', 12)
    eq = int(f'55{x}87', 14)
    if k == eq:
        print(eq)