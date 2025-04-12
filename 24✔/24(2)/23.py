s = open('23.txt').readline()

ky = kx = st = 0
m = 10000000000
for i in range(len(s)):
    if s[i] == 'Y':
        kx = 0
        st = i + 1
    if s[i] == 'X':
        kx += 1
    if kx > 500:
        m = min(m, i - st)
    while kx > 500:
        if s[st] == 'X':
            kx -= 1
        st += 1

print(m)