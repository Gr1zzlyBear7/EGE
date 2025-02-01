ans = []
for n in range(1, 100000):
    bin_n = bin(n)[2:]
    ones = ['1' for x in range(1, len(bin_n), 2) if bin_n[x] == '1']
    zeroes = ['0' for x in range(0, len(bin_n), 2) if bin_n[x] == '0']
    r = abs(len(ones) - len(zeroes))
    if r == 5:
        ans.append(n)
print(min(ans))