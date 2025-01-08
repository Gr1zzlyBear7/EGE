al = ''.join([chr(x) for x in range(ord('a'), ord('z'))])
al = ('0123456789' + al[:11])

for x in al:
    for y in al:
        k = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
        if k % 18:
            break
    else:
        print((int(f'125{x}9', 21) + int(f'36599', 21)) // 18, x)