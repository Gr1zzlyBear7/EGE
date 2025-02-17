s = open('19.txt').readline()
lt = m = kt = 0
for i in range(len(s)):
    if s[i] == 'T':
        kt += 1
    if kt > 100:
        m = max(m, i - lt)
    while kt > 100:
        if s[lt] == 'T':
            kt -= 1
        lt += 1
m = max(m, i - lt)

print(m)