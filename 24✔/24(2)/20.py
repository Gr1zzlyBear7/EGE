s = open('20.txt').readline()
m = st = k = 0
for i in range(1, len(s)):
    if s[i - 1] + s[i] == 'AB':
        k += 1
    if k > 50:
        m = max(m, i - st)
    while k > 50:
        if s[st] + s[st + 1] == 'AB':
            k -= 1
        st += 1
m = max(m, i - st)
print(m)