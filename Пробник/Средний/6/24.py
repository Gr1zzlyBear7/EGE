s = open('24_320.txt').read()
al = ''
for i in range(ord('A'), ord('Z') + 1):
    al += chr(i)
for x in al:
    s = s.replace(x, ' ')
print(max([int(x) for x in s.split() if int(x) % 2 == 0]))