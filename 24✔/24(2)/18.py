s = open('18.txt').readline()
st = 0
kd = 0
m = 0
for i in range(len(s)):
    if s[i] == 'D':
        kd += 1
    if kd > 2:
        m = max(m, i - st)
    while kd > 2:
        if s[st] == 'D':
            kd -= 1
        st += 1
m = max(m, i - st)
print(m)