s = open('24_15339.txt').readline()
s = s.replace('A', 'B').replace('B', 'C')
s = s.replace('6', '7').replace('7', '8')
s = s.replace('8', '9')
m = [1] * len(s)
for i in range(1, len(s)):
    if s[i] + s[i - 1] == 'C9' or s[i] + s[i - 1] == '9C':
        m[i] = m[i - 1] + 1
print(max(m))