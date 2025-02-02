s = open('2506.txt').readline()

m = [1] * len(s)
for i in range(1, len(s)):
    if s[i] + s[i - 1] == 'CC':
        m[i] = m[i - 1] + 1
print(max(m))

s = s.replace('A', ' ').replace('B', ' ')
print(max([len(x) for x in s.split()]))