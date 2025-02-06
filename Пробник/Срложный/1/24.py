s = open('24_505.txt').readline()
m = [1] * len(s)
for i in range(1, len(s)):
    if int(s[i]) + int(s[i - 1]) >= 10:
        m[i] = m[i - 1] + 1
print(max(m))