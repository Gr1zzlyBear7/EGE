s = open('24_7723.txt').read()
s = s.replace('1', '8')
s = s.replace('D', 'R')
m = [0] * len(s)
for i in range(2, len(s)):
    if s[i - 2] + s[i - 1] + s[i] == '88R':
        m[i] = m[i - 3] + 1
print(max(m))