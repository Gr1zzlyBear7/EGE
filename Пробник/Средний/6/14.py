al = '0123456789abc'
for x in al:
    k = int(f'537{x}623', 13) - int(f'6{x}35{x}2', 13)
    if k % 3 == 0:
        print(int(x, 13))