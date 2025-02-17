s = open('17.txt').readline()
m = [0] * len(s)
for i in range(2, len(s)):
    if s[i] + s[i - 2] in ['CC', 'AA']:
        m[i] = m[i - 3] + 1
print(max(m))