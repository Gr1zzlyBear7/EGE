for x in range(0, 15):
    k = (int(f'123{x}5', 15) + int(f'1{x}233', 15))
    if k % 14 == 0:
        print(k // 14)