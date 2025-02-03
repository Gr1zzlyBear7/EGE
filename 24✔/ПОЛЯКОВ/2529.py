s = open('files/2529.txt').readline()
sub = ''
subs = []
for i in range(1, len(s)):
    if s[i - 1] < s[i]:
        if sub:
            sub += s[i]
        else:
            sub += s[i - 1] + s[i]
    else:
        if sub:
            subs.append(sub)
        sub = ''
print((max(subs, key=len)))
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i - 1] < s[i]:
        m[i] = m[i - 1] + 1
        if m[i] == 3:
            print(s[i-2:i + 1])
            break
print(max(m))