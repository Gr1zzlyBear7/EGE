s = open('24_1041.txt').readline()
k = 1
kf = 0
for i in range(len(s)):
    if s[i] == 'f':
        kf += 1
    if kf == 123:
        print(i + 1)
        print(k)
        break
    k += 1