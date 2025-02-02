s = open('2519').readline()
m = [0] * len(s)
for i in range(1, len(s)):
    if s[i] not in 'CF':
        m[i] = m[i - 1] + 1
print(max(m))