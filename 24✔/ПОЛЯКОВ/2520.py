s = open('files/2520').readline()
m = [0] * len(s)
for i in range(1, len(s)):
    if s[i] not in 'AE':
        m[i] = m[i - 1] + 1
print(max(m))