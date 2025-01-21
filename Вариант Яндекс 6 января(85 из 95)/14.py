al = '0123456789abcd'
for y in al:
    x = 'd'
    s = int(f'14{y}5{x}2', 14) + int(f'31{x}2{y}3', 14)
    if s % 9 == 0:
        print(s//9)