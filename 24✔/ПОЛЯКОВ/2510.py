s = open('files/2510.txt').readline()
m = [0] * len(s)
for i in range(2, len(s)):
    if s[i] in 'ABC':
        m[i] = m[i - 1] + 1
print(max(m))