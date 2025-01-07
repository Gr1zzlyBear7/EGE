s = open('3.txt').readline()

s = ''.join([x if x.isdigit() else ' ' for x in s])
k = 0
for line in (s.split()):
    r = len(line)
    if r > k:
        k = r

print(k)