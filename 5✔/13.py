ans = []
for n in range(2, 10000):
    b = bin(n)[2:]
    ones = [1 if b[i] == '1' else 0 for i in range(1, len(b), 2)]
    zero = [0 if b[i] == '0' else 1 for i in range(0, len(b), 2)]
    r = abs(ones.count(1) - zero.count(0))
    if r == 5:
        ans.append(n)
print(min(ans))