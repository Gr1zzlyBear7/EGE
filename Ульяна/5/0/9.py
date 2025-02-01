ans = []
for n in range(28, 100000):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b += '0'
        b = '10' + b[2:]
    else:
        b += '1'
        b = '11' + b[2:]
    r = int(b, 2)
    ans.append(r)
print(min(ans))