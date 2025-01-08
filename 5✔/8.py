ans = []
for n in range(1, 1000):
    b = bin(2 * n)[2:]
    b += str(bin(2 * n)[2:].count('1') % 2)
    b += str(bin(2 * n)[2:].count('1') % 2)
    r = int(b, 2)
    if r > 1017:
        ans.append(n)

print(min(ans))