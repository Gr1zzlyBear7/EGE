ans = []
for n in range(1, 1000):

    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n += bin_n.count('0') * '0'
    else:
        bin_n = bin_n.count('1') * '1' + bin_n
    r = int(bin_n, 2)
    if r > 2000:
        ans.append(n)
print(min(ans))