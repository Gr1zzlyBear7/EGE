s = open('2516').readline()
m = [0] * len(s)
for i in range(1, len(s)):
    if s[i] in 'ACD':
        m[i] = m[i - 1] + 1
print(max(m))