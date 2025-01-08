ans = []
for n in range(1, 1000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n += '01'
    else:
        bin_n += '10'
    r = int(bin_n, 2)
    if r > 81:
        ans.append(r)

print(min(ans))
