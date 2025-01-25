al = '0123456789abcdefghijklmno'
for x in al:
    k = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if k % 24 == 0:
        print(k // 24, x)