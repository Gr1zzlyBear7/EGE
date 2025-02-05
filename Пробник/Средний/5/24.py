s = open('24_1866 (1).txt').readline()
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i] + s[i - 1] != 'da' and s[i] + s[i - 1] != 'ad':
        m[i] = m[i - 1] + 1
print(max(m))