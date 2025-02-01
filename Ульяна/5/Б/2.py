ans = []
for n in range(1, 1000):
    bin_n = bin(n)
    if n % 2 == 0:
        bin_n += '00'
    else:
        bin_n += '11'
    r = int(bin_n, 2)
    if r > 115:
        ans.append(n)
print(min(ans))