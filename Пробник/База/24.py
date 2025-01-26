s = open('24_1866.txt').readline()
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i - 1] + s[i] != 'ad' and s[i - 1] + s[i] != 'da':
        m[i] = m[i - 1] + 1

print(max(m))