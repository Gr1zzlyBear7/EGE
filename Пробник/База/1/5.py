ans = []
for n in range(1, 30):
    bin_n = bin(n)[2:]
    if bin_n.count('1') % 2 == 0:
        bin_n = '10' + bin_n[:-2] + '00'
    else:
        bin_n = '11' + bin_n[:-2] + '11'
    r = int(bin_n, 2)
    ans.append(r)
print(max(ans))