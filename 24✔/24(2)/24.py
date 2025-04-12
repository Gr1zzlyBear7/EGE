s = open('24.txt').readline()

m = 1000000
k = st = 0
for i in range(2, len(s)):
    if s[i - 2] + s[i - 1] + s[i] in ['BAD', 'FAT']:
        k += 1
    while k == 3:
        m = min(m, i - st + 1)
        if s[st] + s[st + 1] + s[st + 2] in ['BAD', 'FAT']:
            k -= 1
        st += 1

print(m)