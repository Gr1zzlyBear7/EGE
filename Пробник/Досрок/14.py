al = '0123456789'
for x in range(ord('a'), ord('z')):
    al += chr(x)
al = '0123456789abcdefghijk'
for x in al:
    k = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
    if k % 20 == 0:
        if x == '3':
            print(k // 20)