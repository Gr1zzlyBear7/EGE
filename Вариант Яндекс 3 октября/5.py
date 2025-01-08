ans = []
for i in range(1, 1000):
    bin_n = bin(i)[2:]
    bin_n += str(sum(map(int, bin_n)) % 2)
    bin_n += str(sum(map(int, bin_n)) % 2)
    r = int(bin_n, 2)
    if r > 198:
        ans.append(r)
print(min(ans))