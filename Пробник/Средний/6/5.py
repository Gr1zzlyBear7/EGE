al = '0123456789abcdef'
ev = [al[x] for x in range(0, len(al), 2)]
ans = []
for n in range(151, 10000):
    h = hex(n)[2:]
    h = h.replace('a', '1')
    c1 = [x for x in range(len(h)) if h[x] in ev]
    if len(c1) > 2:
        h += 'b'
    else:
        h = 'f' + h
    r = int(h, 16)
    if r > 3500:
        ans.append(n)
        print(r)
print(min(ans))