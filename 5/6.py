ans = []
for n in range(1, 101):
    b = bin(n)[2:]
    r = int(str(int(b[::-1])), 2)
    if r == 13:
        ans.append(n)

print(max(ans))

