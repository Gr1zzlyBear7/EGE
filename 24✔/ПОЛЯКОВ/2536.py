s = open('files/24-1.txt').readline()
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i - 1] > s[i]:
        m[i] = m[i - 1] + 1
        if m[i] == 8:
            print(i - 7 + 1)
            break
print(max(m))