for x in range(0, 18):
    k = int(f'9759{x}', 17) + int(f'3{x}108', 17)
    if k % 11 == 0:
        print(k // 11)