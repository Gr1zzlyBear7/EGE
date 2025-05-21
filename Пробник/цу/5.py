ans = []
for n in range(1, 10000):
    b = bin(n)[2:]
    if sum(map(int, str(n))) % 2 != 0:
        b += '1'
    else:
        b += '0'
    n = int(b, 2)
    if sum(map(int, str(n))) % 2 != 0:
        b += '1'
    else:
        b += '0'
    n = int(b, 2)
    if sum(map(int, str(n))) % 2 != 0:
        b += '1'
    else:
        b += '0'
    r = int(b, 2)
    if r > 2025:
        ans.append(r)
print(min(ans))