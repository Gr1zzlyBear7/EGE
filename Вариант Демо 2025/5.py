ans = []
for i in range(1, 13):
    bin_n = bin(i)[2:]
    bin_n = '10' + bin_n if i % 2 == 0 else '1' + bin_n + '01'
    r = int(bin_n, 2)
    ans.append(r)

print(max(ans))