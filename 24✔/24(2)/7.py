s = open('7.txt').readline()

flag = False
k = 0
ma = 0
for i in range(0, len(s) - 2, 3):
    tri = s[i:i+3]
    if 'NPO' in tri or 'PNO' in tri:
        flag = True
    else:
        flag = False
    if flag:
        k += 1
    else:
        if k > ma:
            ma = k
        k = 0

print(ma)
