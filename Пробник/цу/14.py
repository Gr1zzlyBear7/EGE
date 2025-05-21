for x in '0123456789abcde':
    k = int(f'97968{x}15', 15) + int(f'7{x}233', 15)
    if k % 14 == 0:
        print(x)
        print(k // 14)