s = open('2532.txt').readline()
sub = ''
m = [1] * len(s)
subs = []
for i in range(1, len(s)):
    if s[i - 1] < s[i]:
        m[i] = m[i - 1] + 1
        if m[i] == 7:
            print(i - 6)
            break
print(max(m))