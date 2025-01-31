s = open('24_2250.txt').readline()
m = 0
s = s.split('A')
for i in range(len(s) - 1):
    m = max(len(s[i]) + 1 + len(s[i + 1]), m)
print(m)