s = open('14.txt').readline()
k = ma = 0
m = []
ind = 0
for i in range(len(s) - 1):
    if ord(s[i]) > ord(s[i + 1]):
        pass
    else:
        m.append([len(s[ind:i + 2]), s[ind:i + 2]])
        ind = i + 1
m.append([len(s[ind:i + 2]), s[ind:i + 2]])
print(max(m))