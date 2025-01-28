s = open('24_18029.txt').readline()
l = my = kx = ky = 0
mx = 1000
for r in range(len(s)):
    if s[r] == 'X':
        kx += 1
    if s[r] == 'Y':
        ky += 1
    while kx > 2:
        if s[l] == 'X':
            kx -= 1
        if s[l] == 'Y':
            ky -= 1
        l += 1
    my = max(my, ky)
    mx = min(mx, r - l + 1)
print(mx, my)
