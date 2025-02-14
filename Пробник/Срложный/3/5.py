ans = []
for n in range(1, 10000):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = '1' + b[:-2] + '11'
    else:
        b = '10' + b + '0'
    r = int(b, 2)
    if n % 2 == 0:
        if r > 999:
            ans.append(r)
            print(n)
print(min(ans))