s = open('2517').readline()
m = [0] * len(s)
for i in range(1, len(s)):
    if s[i] in 'ABEF':
        m[i] = m[i - 1] + 1
print(max(m))