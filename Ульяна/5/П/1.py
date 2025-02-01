ans = []
for n in range(1, 1000):
    bin_n = bin(n)[2:]
    if n % 4 == 0:
        bin_n += bin_n[-2:]
    else:
        bin_n += bin(n % 4)[2:]
    if bin_n[-1] == '0':
        bin_n = bin_n[:-1]
    r = int(bin_n, 2)
    if r > 213:
        ans.append(r)
print(min(ans))