al = ''.join([str(X) for X in range(0, 10)])
for i in range(ord('a'), ord('z')):
    al += chr(i)
al = (al[:17])
for x in al:
    k = int(f'5432{x}67', 17) + int(f'302{x}', 17)
    if k % 19 == 0:
        print(x, k)