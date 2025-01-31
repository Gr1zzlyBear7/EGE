ans = set()
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    bin_n += str(bin_n.count('1') % 2)
    bin_n += str(bin_n.count('1') % 2)
    r = int(bin_n, 2)
    if 20 <= r <= 50:
        ans.add(r)
print(len(ans))
