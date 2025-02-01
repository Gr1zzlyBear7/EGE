ans = []
for n in range(1, 1000):
    bin_n = bin(n)[2:]
    bin_n += bin_n[-1]
    if bin_n.count('1') % 2 == 0:
        bin_n += '0'
    else:
        bin_n += '1'
    if bin_n.count('1') % 2 == 0:
        bin_n += '0'
    else:
        bin_n += '1'
    r = int(bin_n, 2)
    if r > 136:
        ans.append(n)
print(min(ans))