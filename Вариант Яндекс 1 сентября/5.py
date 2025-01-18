ans = []
for n in range(26, 100):
    bin_n = bin(n)[2:]
    if n % 2 != 0:
        bin_n = bin_n[:-2] + '10'
    else:
        bin_n = '10' + bin_n[2:] + '1'
    r = int(bin_n, 2)
    ans.append([r, n])
print(min(ans))
