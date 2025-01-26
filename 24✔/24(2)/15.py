s = open('15.txt').readline()
m = [0] * len(s)
for i in range(1, len(s)):
    if s[i] + s[i - 1] == 'BB' or s[i] + s[i - 1] == 'DD':
        m[i] = m[i - 2] + 1
print(max(m))