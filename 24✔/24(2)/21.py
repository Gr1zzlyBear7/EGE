s = open('21.txt').readline()
k = st = m = 0
s = 'OROAAAAARODSADSADADSADSROR'
for i in range(1, len(s)):
    if s[i - 1] + s[i] == 'R0':
        k += 1
    while k > 21:
        sub = s[st:i]
        while 'ORO' in sub or 'ROR' in sub:
            sub = sub[st:i]
            st += 1
