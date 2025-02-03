ans = []
for n in range(1, 100):
    b = bin(n)[2:]
    b = str(int(b[::-1]))
    r = int(b, 2)
    if r == 13:
        print(n)