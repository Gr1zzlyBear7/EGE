s = open('files/2507').readline()
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        m[i] = m[i - 1] + 1
        if m[i] == 9:
            print(s[i])
print(max(m))
