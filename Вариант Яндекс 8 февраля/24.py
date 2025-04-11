s = open('24 (20).txt').readline()
al = ''
for i in range(ord('A'), ord('Z') + 1):
    al += chr(i)
for x in al:
    s = s.replace(x, ' ')
s = s.split()
new = sorted(s, key=len, reverse=True)
for i in new:
    print(i)