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


ans = []
for i in range(len(data) - 2):
    tri = [data[i], data[i + 1], data[i + 2]]
    c1 = []
    for elem in tri:
        if abs(elem) % 10 == 3 or abs(elem) % 10 == 5:
            c1.append(elem)
    if len(c1) > 1:
        ans.append(sum(tri))
print(len(ans))
