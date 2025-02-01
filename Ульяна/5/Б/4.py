ans = []
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    if bin_n.count('1') % 2 == 0:
        bin_n = '1' + bin_n + '00'
    else:
        bin_n = '11' + bin_n
    r = int(bin_n, 2)
    if r >= 412:
        ans.append(n)
print(min(ans))