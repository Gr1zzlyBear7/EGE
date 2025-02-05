ans = []
for n in range(1, 10000):
    b = bin(n)[2:]
    b += b[-1]
    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    if b.count('1') % 2 == 0:
        b += '0'
    else:
        b += '1'
    r = int(b, 2)
    if r > 114:
        ans.append(r)
print(min(ans))